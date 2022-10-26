"""
This is a module containing tasks for interacting with:
Hightouch syncs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-10-26T03:21:11.836263

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client.api.default.get_sync import asyncio


@task
async def trigger_run_custom(
    hightouch_credentials: "HightouchCredentials",
    sync_slug: Optional[str] = None,
    sync_id: Optional[str] = None,
    full_resync: bool = False,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Trigger a new run globally based on sync id or sync slug  If a run is already in
    progress, this queues a sync run that will get executed immediately after
    the current run completes.

    Args:
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.
        sync_slug:
            Trigger run based on sync slug.
        sync_id:
            Trigger run based on sync id.
        full_resync:
            Whether to resync all the rows in the query (i.e. ignoring previously
            synced rows).

    Returns:
        Upon success, a dict of the response. </br>- `id: str`</br>- `message: str`</br>- `details: Dict`</br>

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
    client = hightouch_credentials.get_client()
    parsed = await asyncio(
        sync_slug=sync_slug, sync_id=sync_id, full_resync=full_resync, client=client
    )
    return parsed
