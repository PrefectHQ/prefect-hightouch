"""
This is a module containing tasks for interacting with:
Hightouch syncs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-10-26T03:21:11.837919

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client.api.default.get_sync import asyncio


@task
async def trigger_run(
    sync_id: str,
    hightouch_credentials: "HightouchCredentials",
    full_resync: bool = False,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Trigger a new run for the given sync.  If a run is already in progress, this
    queues a sync run that will get executed immediately after the current run
    completes.

    Args:
        sync_id:
            Sync ID used in formatting the endpoint URL.
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.
        full_resync:
            Whether to resync all the rows in the query (i.e. ignoring previously
            synced rows).

    Returns:
        Upon success, a dict of the response. </br>- `id: str`</br>

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
    client = hightouch_credentials.get_client()
    parsed = await asyncio(full_resync=full_resync, client=client)
    return parsed
