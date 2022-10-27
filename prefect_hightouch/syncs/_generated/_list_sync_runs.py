"""
This is a module containing tasks for interacting with:
Hightouch syncs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-10-27T03:04:31.820092

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client import api, models, types  # noqa
from prefect_hightouch.api_client.api.default.list_sync_runs import asyncio as request


@task
async def list_sync_runs(
    sync_id: float,
    hightouch_credentials: "HightouchCredentials",
    run_id: Union[types.Unset, None, float] = types.UNSET,
    limit: Union[types.Unset, None, float] = types.UNSET,
    offset: Union[types.Unset, None, float] = types.UNSET,
    after: Union[types.Unset, None, datetime.datetime] = types.UNSET,
    before: Union[types.Unset, None, datetime.datetime] = types.UNSET,
    within: Union[types.Unset, None, float] = types.UNSET,
    order_by: Union[
        types.Unset, None, models.list_sync_runs_order_by.ListSyncRunsOrderBy
    ] = id,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List all sync runs under a sync.

    Args:
        sync_id:
            Sync ID used in formatting the endpoint URL.
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.
        run_id:
            query for specific run id.
        limit:
            limit the number of object it returns. Default is 5.
        offset:
            setting offset from result(for pagination).
        after:
            select sync runs that are started after given timestamp.
        before:
            select sync runs that are started before certain timestamp.
        within:
            select sync runs that are started within last given minutes.
        order_by:
            specify the order.

    Returns:
        Upon success, a dict of the response. </br>- `data: List`</br>

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
    client = hightouch_credentials.get_client()
    parsed = await request(
        sync_id=sync_id,
        hightouch_credentials=hightouch_credentials,
        run_id=run_id,
        limit=limit,
        offset=offset,
        after=after,
        before=before,
        within=within,
        order_by=order_by,
        client=client,
    )
    return parsed
