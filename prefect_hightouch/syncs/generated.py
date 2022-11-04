"""
This is a module containing tasks, auto-generated from the Hightouch
REST schema, used for interacting with syncs.
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module is outdated
# rerun scripts/generate.py. To override the default generated output:
# 1. create a separate module and rewrite the class / function
# 2. import in `__init__.py`, under the `from .generated import *` line
# 3. hide the generated function in `docs/syncs.md` under `options`

# OpenAPI spec: swagger.yaml
# Updated at: 2022-11-04T18:46:27.586065

import typing

from prefect import task

from prefect_hightouch.api_client import models as api_models
from prefect_hightouch.api_client.api import _update_kwargs_and_execute
from prefect_hightouch.api_client.api.default.get_sync import (
    asyncio as _get_sync_endpoint,
)
from prefect_hightouch.api_client.api.default.list_sync import (
    asyncio as _list_sync_endpoint,
)
from prefect_hightouch.api_client.api.default.list_sync_runs import (
    asyncio as _list_sync_runs_endpoint,
)
from prefect_hightouch.api_client.api.default.trigger_run import (
    asyncio as _trigger_run_endpoint,
)
from prefect_hightouch.api_client.api.default.trigger_run_custom import (
    asyncio as _trigger_run_custom_endpoint,
)


@task
@_update_kwargs_and_execute(_list_sync_endpoint)
async def list_sync(*args, **kwargs) -> typing.List[api_models.sync.Sync]:
    """
    List all the syncs in the current workspace.

    Args:
        hightouch_credentials (HightouchCredentials):
            Credentials to use for authentication with Hightouch.
        slug (Optional[str]]):
            Filter based on slug.
        model_id (Optional[float]]):
            Filter based on modelId.
        after (Optional[datetime.datetime]]):
            Select syncs that were run after given time.
        before (Optional[datetime.datetime]]):
            Select syncs that were run before given time.
        limit (Optional[float]]):
            Limit the number of object it returns. Default is 100.
        order_by (Optional[models.list_sync_order_by.ListSyncOrderBy]]):
            Specify the order.

    Returns:
        typing.List[api_models.sync.Sync]:
        - `data: List`

    <h4>API Endpoint:</h4>
    `/syncs`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 422 | Validation Failed. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_trigger_run_custom_endpoint)
async def trigger_run_custom(
    *args, **kwargs
) -> api_models.trigger_run_output.TriggerRunOutput:
    """
    Trigger a new run globally based on sync id or sync slug  If a run is already in
    progress, this queues a sync run that will get executed immediately after
    the current run completes.

    Args:
        hightouch_credentials (HightouchCredentials):
            Credentials to use for authentication with Hightouch.
        json_body (models.trigger_run_custom_input.TriggerRunCustomInput):
            The input of a trigger action to run syncs based on sync ID, slug or
            other filters.

    Returns:
        api_models.trigger_run_output.TriggerRunOutput:
        - `id: str`
        - `message: str`
        - `details: Dict`

    <h4>API Endpoint:</h4>
    `/syncs/trigger`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 422 | Validation Failed. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_get_sync_endpoint)
async def get_sync(*args, **kwargs) -> api_models.sync.Sync:
    """
    Retrieve sync from sync ID.

    Args:
        hightouch_credentials (HightouchCredentials):
            Credentials to use for authentication with Hightouch.
        sync_id (float):
            Sync ID used in formatting the endpoint URL.

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

    <h4>API Endpoint:</h4>
    `/syncs/{sync_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 401 | Unauthorized. |
    | 404 | Not found. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_list_sync_runs_endpoint)
async def list_sync_runs(*args, **kwargs) -> typing.List[api_models.sync_run.SyncRun]:
    """
    List all sync runs under a sync.

    Args:
        hightouch_credentials (HightouchCredentials):
            Credentials to use for authentication with Hightouch.
        sync_id (float):
            Sync ID used in formatting the endpoint URL.
        run_id (Optional[float]]):
            Query for specific run id.
        limit (Optional[float]]):
            Limit the number of object it returns. Default is 5.
        offset (Optional[float]]):
            Setting offset from result(for pagination).
        after (Optional[datetime.datetime]]):
            Select sync runs that are started after given timestamp.
        before (Optional[datetime.datetime]]):
            Select sync runs that are started before certain timestamp.
        within (Optional[float]]):
            Select sync runs that are started within last given minutes.
        order_by (Optional[models.list_sync_runs_order_by.ListSyncRunsOrderBy]]):
            Specify the order.

    Returns:
        typing.List[api_models.sync_run.SyncRun]:
        - `data: List`

    <h4>API Endpoint:</h4>
    `/syncs/{sync_id}/runs`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 422 | Validation Failed. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_trigger_run_endpoint)
async def trigger_run(
    *args, **kwargs
) -> api_models.trigger_run_output.TriggerRunOutput:
    """
    Trigger a new run for the given sync.  If a run is already in progress, this
    queues a sync run that will get executed immediately after the current run
    completes.

    Args:
        hightouch_credentials (HightouchCredentials):
            Credentials to use for authentication with Hightouch.
        sync_id (str):
            Sync ID used in formatting the endpoint URL.
        json_body (models.trigger_run_input.TriggerRunInput):
            The input of a trigger action to run syncs.

    Returns:
        api_models.trigger_run_output.TriggerRunOutput:
        - `id: str`

    <h4>API Endpoint:</h4>
    `/syncs/{sync_id}/trigger`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 422 | Validation Failed. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run
