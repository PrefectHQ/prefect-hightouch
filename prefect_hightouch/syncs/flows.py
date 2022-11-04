"""
This is a module containing flows used for interacting with syncs.
"""

import asyncio
from typing import Tuple

from prefect import flow, get_run_logger

from prefect_hightouch.api_client.models import Sync, SyncStatus, TriggerRunInput
from prefect_hightouch.credentials.generated import HightouchCredentials
from prefect_hightouch.exceptions import (
    TERMINAL_STATUS_EXCEPTIONS,
    HightouchSyncRunError,
    HightouchSyncRunTimedOut,
)
from prefect_hightouch.syncs import get_sync, trigger_run


@flow
async def trigger_sync_run_and_wait_for_completion(
    hightouch_credentials: HightouchCredentials,
    sync_id: str,
    full_resync: bool = False,
    max_wait_seconds: int = 900,
    poll_frequency_seconds: int = 10,
) -> Sync:
    """
    Flow that triggers a sync run and waits for the triggered run to complete.

    Args:
        hightouch_credentials: Credentials to use for authentication with Hightouch.
        sync_id: Sync ID used in formatting the endpoint URL.
        full_resync: Whether to resync all the rows in the query
            (i.e. ignoring previously synced rows).
        max_wait_seconds: Maximum number of seconds to wait for the entire
            flow to complete.
        poll_frequency_seconds: Number of seconds to wait in between checks for
            run completion.

    Returns:
        api_models.sync.Sync:
        - `id: str`
        - `slug: str`
        - `workspace_id: str`
        - `created_at: str`
        - `updated_at: str`
        - `destination_id: str`
        - `model_id: str`
        - `configuration: Dict`
        - `schedule: Dict`
        - `status: "models.SyncStatus"`
        - `disabled: bool`
        - `last_run_at: str`
        - `referenced_columns: List[str]`
        - `primary_key: str`

    Examples:
        Trigger a Hightouch sync run and wait for completion as a stand alone flow.
        ```python
        import asyncio

        from prefect_hightouch import HightouchCredentials
        from prefect_hightouch.syncs import trigger_sync_run_and_wait_for_completion

        asyncio.run(
            trigger_sync_run_and_wait_for_completion(
                hightouch_credentials=HightouchCredentials(
                    token="1abc0d23-1234-1a2b-abc3-12ab456c7d8e"
                ),
                sync_id=12345,
                full_resync=True,
                max_wait_seconds=1800,
                poll_frequency_seconds=5,
            )
        )
        ```

        Trigger a Hightouch sync run and wait for completion as a subflow.
        ```python
        from prefect import flow

        from prefect_hightouch import HightouchCredentials
        from prefect_hightouch.syncs import trigger_sync_run_and_wait_for_completion

        @flow
        def sync_flow():
            hightouch_credentials = HightouchCredentials.load("hightouch-token")
            sync_metadata = trigger_sync_run_and_wait_for_completion(
                hightouch_credentials=hightouch_credentials,
                sync_id=12345,
                full_resync=True,
                max_wait_seconds=1800,
                poll_frequency_seconds=10,
            )
            return sync_metadata

        sync_flow()
        ```
    """
    logger = get_run_logger()

    json_body = TriggerRunInput(full_resync=full_resync)
    sync_run_future = await trigger_run.submit(
        hightouch_credentials=hightouch_credentials,
        sync_id=sync_id,
        json_body=json_body,
    )
    sync_run = await sync_run_future.result()
    logger.info(
        "Started sync %s run %s; open %s and append %s to view results on webpage.",
        repr(sync_id),
        repr(sync_run.id),
        "https://app.hightouch.com/",
        f"/sources/{sync_id}/runs/{sync_run.id}",
    )

    sync_status, sync_metadata = await wait_for_sync_run_completion(
        hightouch_credentials=hightouch_credentials,
        sync_id=sync_id,
        max_wait_seconds=max_wait_seconds,
        poll_frequency_seconds=poll_frequency_seconds,
    )

    if sync_status == SyncStatus.SUCCESS:
        return sync_metadata
    else:
        raise TERMINAL_STATUS_EXCEPTIONS.get(sync_status, HightouchSyncRunError)(
            f"Sync ({sync_metadata.slug!r}, ID {sync_id!r}) "
            f"was unsuccessful with {sync_status.value!r} status"
        )


@flow
async def wait_for_sync_run_completion(
    hightouch_credentials: HightouchCredentials,
    sync_id: str,
    max_wait_seconds: int = 900,
    poll_frequency_seconds: int = 10,
) -> Tuple[SyncStatus, Sync]:
    """
    Flow that waits for the triggered sync run to complete.

    Args:
        hightouch_credentials: Credentials to use for authentication with Hightouch.
        sync_id: Sync ID used in formatting the endpoint URL.
        max_wait_seconds: Maximum number of seconds to wait for the
            entire flow to complete.
        poll_frequency_seconds: Number of seconds to wait in between checks for
            run completion.

    Returns:
        (sync_status, sync_metadata):
        - `SyncStatus` object
        - `Sync` object

    Examples:
        Wait for completion as a subflow.
        ```python
        from prefect import flow

        from prefect_hightouch import HightouchCredentials
        from prefect_hightouch.syncs import wait_for_sync_run_completion

        @flow
        def wait_flow():
            hightouch_credentials = HightouchCredentials.load("hightouch-token")
            sync_status, sync_metadata = wait_for_sync_run_completion(
                hightouch_credentials=hightouch_credentials,
                sync_id=12345,
                max_wait_seconds=1800,
                poll_frequency_seconds=20,
            )
            return sync_metadata

        wait_flow()
        ```
    """
    logger = get_run_logger()
    seconds_waited_for_run_completion = 0
    wait_for = []

    while seconds_waited_for_run_completion <= max_wait_seconds:
        sync_future = await get_sync.submit(
            hightouch_credentials=hightouch_credentials,
            sync_id=sync_id,
            wait_for=wait_for,
        )
        wait_for = [sync_future]

        sync_metadata = await sync_future.result()
        sync_slug = sync_metadata.slug
        sync_status = sync_metadata.status
        if sync_status in TERMINAL_STATUS_EXCEPTIONS.keys():
            return sync_status, sync_metadata

        logger.info(
            "Waiting on sync (%s, ID %s) with sync status %s for %s seconds",
            repr(sync_slug),
            repr(sync_id),
            repr(sync_status.value),
            poll_frequency_seconds,
        )
        await asyncio.sleep(poll_frequency_seconds)
        seconds_waited_for_run_completion += poll_frequency_seconds

    raise HightouchSyncRunTimedOut(
        f"Max wait time of {max_wait_seconds} seconds exceeded while waiting "
        f"for sync ({sync_slug!r}, ID {sync_id!r})"
    )
