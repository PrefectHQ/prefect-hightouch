from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from prefect import task

from ....credentials import HightouchCredentials
from ...client import AuthenticatedClient
from ...models.list_source_order_by import ListSourceOrderBy
from ...models.list_source_response_200 import ListSourceResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    slug: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSourceOrderBy] = ListSourceOrderBy.ID,
) -> Dict[str, Any]:
    url = "{}/sources".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["name"] = name

    params["slug"] = slug

    params["limit"] = limit

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
) -> Optional[Union[Any, ListSourceResponse200]]:
    if response.status_code == 200:
        response_200 = ListSourceResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, ListSourceResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    slug: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSourceOrderBy] = ListSourceOrderBy.ID,
) -> Response[Union[Any, ListSourceResponse200]]:
    """List Sources

     List all the sources in the current workspace

    Args:
        name (Union[Unset, None, str]):
        slug (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSourceOrderBy]):  Default: ListSourceOrderBy.ID.

    Returns:
        Response[Union[Any, ListSourceResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        slug=slug,
        limit=limit,
        order_by=order_by,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    slug: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSourceOrderBy] = ListSourceOrderBy.ID,
) -> Optional[Union[Any, ListSourceResponse200]]:
    """List Sources

     List all the sources in the current workspace

    Args:
        name (Union[Unset, None, str]):
        slug (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSourceOrderBy]):  Default: ListSourceOrderBy.ID.

    Returns:
        Response[Union[Any, ListSourceResponse200]]
    """

    return sync_detailed(
        client=client,
        name=name,
        slug=slug,
        limit=limit,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    slug: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSourceOrderBy] = ListSourceOrderBy.ID,
) -> Response[Union[Any, ListSourceResponse200]]:
    """List Sources

     List all the sources in the current workspace

    Args:
        name (Union[Unset, None, str]):
        slug (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSourceOrderBy]):  Default: ListSourceOrderBy.ID.

    Returns:
        Response[Union[Any, ListSourceResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        slug=slug,
        limit=limit,
        order_by=order_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    slug: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSourceOrderBy] = ListSourceOrderBy.ID,
) -> Optional[Union[Any, ListSourceResponse200]]:
    """List Sources

     List all the sources in the current workspace

    Args:
        name (Union[Unset, None, str]):
        slug (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSourceOrderBy]):  Default: ListSourceOrderBy.ID.

    Returns:
        Response[Union[Any, ListSourceResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            slug=slug,
            limit=limit,
            order_by=order_by,
        )
    ).parsed


@task(name="ListSource")
async def asyncio_task(
    hightouch_credentials: HightouchCredentials,
    name: Union[Unset, None, str] = UNSET,
    slug: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSourceOrderBy] = ListSourceOrderBy.ID,
) -> Optional[Union[Any, ListSourceResponse200]]:
    """List Sources

     List all the sources in the current workspace

    Args:
        name (Union[Unset, None, str]):
        slug (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSourceOrderBy]):  Default: ListSourceOrderBy.ID.

    Returns:
        Response[Union[Any, ListSourceResponse200]]
    """

    client = hightouch_credentials.get_client()
    return await asyncio(
        client=client,
        name=name,
        slug=slug,
        limit=limit,
        order_by=order_by,
    )
