import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from prefect import task

from ....credentials import HightouchCredentials
from ...client import AuthenticatedClient
from ...models.list_sync_runs_order_by import ListSyncRunsOrderBy
from ...models.list_sync_runs_response_200 import ListSyncRunsResponse200
from ...models.validate_error_json import ValidateErrorJSON
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sync_id: float,
    *,
    client: AuthenticatedClient,
    run_id: Union[Unset, None, float] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    offset: Union[Unset, None, float] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    within: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSyncRunsOrderBy] = ListSyncRunsOrderBy.ID,
) -> Dict[str, Any]:
    url = "{}/syncs/{syncId}/runs".format(client.base_url, syncId=sync_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["runId"] = run_id

    params["limit"] = limit

    params["offset"] = offset

    json_after: Union[Unset, None, str] = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat() if after else None

    params["after"] = json_after

    json_before: Union[Unset, None, str] = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat() if before else None

    params["before"] = json_before

    params["within"] = within

    json_order_by: Union[Unset, None, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value if order_by else None

    params["orderBy"] = json_order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, ListSyncRunsResponse200, ValidateErrorJSON]]:
    if response.status_code == 200:
        response_200 = ListSyncRunsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 422:
        response_422 = ValidateErrorJSON.from_dict(response.json())

        return response_422
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, ListSyncRunsResponse200, ValidateErrorJSON]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    sync_id: float,
    *,
    client: AuthenticatedClient,
    run_id: Union[Unset, None, float] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    offset: Union[Unset, None, float] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    within: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSyncRunsOrderBy] = ListSyncRunsOrderBy.ID,
) -> Response[Union[Any, ListSyncRunsResponse200, ValidateErrorJSON]]:
    """List Sync Runs

     List all sync runs under a sync

    Args:
        sync_id (float):
        run_id (Union[Unset, None, float]):
        limit (Union[Unset, None, float]):
        offset (Union[Unset, None, float]):
        after (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        within (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSyncRunsOrderBy]):  Default: ListSyncRunsOrderBy.ID.

    Returns:
        Response[Union[Any, ListSyncRunsResponse200, ValidateErrorJSON]]
    """

    kwargs = _get_kwargs(
        sync_id=sync_id,
        client=client,
        run_id=run_id,
        limit=limit,
        offset=offset,
        after=after,
        before=before,
        within=within,
        order_by=order_by,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    sync_id: float,
    *,
    client: AuthenticatedClient,
    run_id: Union[Unset, None, float] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    offset: Union[Unset, None, float] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    within: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSyncRunsOrderBy] = ListSyncRunsOrderBy.ID,
) -> Optional[Union[Any, ListSyncRunsResponse200, ValidateErrorJSON]]:
    """List Sync Runs

     List all sync runs under a sync

    Args:
        sync_id (float):
        run_id (Union[Unset, None, float]):
        limit (Union[Unset, None, float]):
        offset (Union[Unset, None, float]):
        after (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        within (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSyncRunsOrderBy]):  Default: ListSyncRunsOrderBy.ID.

    Returns:
        Response[Union[Any, ListSyncRunsResponse200, ValidateErrorJSON]]
    """

    return sync_detailed(
        sync_id=sync_id,
        client=client,
        run_id=run_id,
        limit=limit,
        offset=offset,
        after=after,
        before=before,
        within=within,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    sync_id: float,
    *,
    client: AuthenticatedClient,
    run_id: Union[Unset, None, float] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    offset: Union[Unset, None, float] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    within: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSyncRunsOrderBy] = ListSyncRunsOrderBy.ID,
) -> Response[Union[Any, ListSyncRunsResponse200, ValidateErrorJSON]]:
    """List Sync Runs

     List all sync runs under a sync

    Args:
        sync_id (float):
        run_id (Union[Unset, None, float]):
        limit (Union[Unset, None, float]):
        offset (Union[Unset, None, float]):
        after (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        within (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSyncRunsOrderBy]):  Default: ListSyncRunsOrderBy.ID.

    Returns:
        Response[Union[Any, ListSyncRunsResponse200, ValidateErrorJSON]]
    """

    kwargs = _get_kwargs(
        sync_id=sync_id,
        client=client,
        run_id=run_id,
        limit=limit,
        offset=offset,
        after=after,
        before=before,
        within=within,
        order_by=order_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    sync_id: float,
    *,
    client: AuthenticatedClient,
    run_id: Union[Unset, None, float] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    offset: Union[Unset, None, float] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    within: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSyncRunsOrderBy] = ListSyncRunsOrderBy.ID,
) -> Optional[Union[Any, ListSyncRunsResponse200, ValidateErrorJSON]]:
    """List Sync Runs

     List all sync runs under a sync

    Args:
        sync_id (float):
        run_id (Union[Unset, None, float]):
        limit (Union[Unset, None, float]):
        offset (Union[Unset, None, float]):
        after (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        within (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSyncRunsOrderBy]):  Default: ListSyncRunsOrderBy.ID.

    Returns:
        Response[Union[Any, ListSyncRunsResponse200, ValidateErrorJSON]]
    """

    return (
        await asyncio_detailed(
            sync_id=sync_id,
            client=client,
            run_id=run_id,
            limit=limit,
            offset=offset,
            after=after,
            before=before,
            within=within,
            order_by=order_by,
        )
    ).parsed


@task(name="ListSyncRuns")
async def asyncio_task(
    hightouch_credentials: HightouchCredentials,
    sync_id: float,
    run_id: Union[Unset, None, float] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    offset: Union[Unset, None, float] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    within: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSyncRunsOrderBy] = ListSyncRunsOrderBy.ID,
) -> Optional[Union[Any, ListSyncRunsResponse200, ValidateErrorJSON]]:
    """List Sync Runs

     List all sync runs under a sync

    Args:
        sync_id (float):
        run_id (Union[Unset, None, float]):
        limit (Union[Unset, None, float]):
        offset (Union[Unset, None, float]):
        after (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        within (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSyncRunsOrderBy]):  Default: ListSyncRunsOrderBy.ID.

    Returns:
        Response[Union[Any, ListSyncRunsResponse200, ValidateErrorJSON]]
    """

    client = hightouch_credentials.get_client()
    return await asyncio(
        sync_id=sync_id,
        client=client,
        run_id=run_id,
        limit=limit,
        offset=offset,
        after=after,
        before=before,
        within=within,
        order_by=order_by,
    )