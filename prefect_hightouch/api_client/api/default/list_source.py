"""
This is a module containing functions, auto-generated from the 
REST schema, but note these are **not** Prefect tasks.

Example usage shown below; be sure to replace `endpoint_fn` with the desired endpoint function.

```python
from prefect_hightouch.credentials import HightouchCredentials
from prefect_hightouch.api_client.api.default import endpoint_fn

credentials = HightouchCredentials(token="my-service-token")
client = credentials.get_client()
result = endpoint_fn.sync(client=client)
```

The functions are described below:

- `asyncio`: Non-blocking request that returns parsed data (if successful) or None. Any calls must be awaited.
- `asyncio_detailed`: Non-blocking request that always returns a Request, optionally with parsed set if the request was successful. Any calls must be awaited.
- `sync`: Blocking request that returns parsed data (if successful) or None.
- `sync_detailed`: Blocking request that always returns a Request, optionally with parsed set if the request was successful.
"""

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.list_source_order_by import ListSourceOrderBy
from ...models.list_source_response_200 import ListSourceResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
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

    kwargs = {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }

    if "json" in kwargs:
        kwargs["json"] = {k: v for k, v in kwargs["json"].items() if v != UNSET}
    return kwargs


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, ListSourceResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListSourceResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, ListSourceResponse200]]:
    response.raise_for_status()

    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    slug: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSourceOrderBy] = ListSourceOrderBy.ID,
) -> Response[Union[Any, ListSourceResponse200]]:
    """List Sources

     List all the sources in the current workspace

    Args:
        client: An authenticated client.
        name (Union[Unset, None, str]):
        slug (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSourceOrderBy]):  Default: ListSourceOrderBy.ID.

    Returns:
        The response.
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
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    slug: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSourceOrderBy] = ListSourceOrderBy.ID,
) -> Optional[Union[Any, ListSourceResponse200]]:
    """List Sources

     List all the sources in the current workspace

    Args:
        client: An authenticated client.
        name (Union[Unset, None, str]):
        slug (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSourceOrderBy]):  Default: ListSourceOrderBy.ID.

    Returns:
        The parsed response.
    """

    return sync_detailed(
        client=client,
        name=name,
        slug=slug,
        limit=limit,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    slug: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSourceOrderBy] = ListSourceOrderBy.ID,
) -> Response[Union[Any, ListSourceResponse200]]:
    """List Sources

     List all the sources in the current workspace

    Args:
        client: An authenticated client.
        name (Union[Unset, None, str]):
        slug (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSourceOrderBy]):  Default: ListSourceOrderBy.ID.

    Returns:
        The response.
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
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    slug: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSourceOrderBy] = ListSourceOrderBy.ID,
) -> Optional[Union[Any, ListSourceResponse200]]:
    """List Sources

     List all the sources in the current workspace

    Args:
        client: An authenticated client.
        name (Union[Unset, None, str]):
        slug (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSourceOrderBy]):  Default: ListSourceOrderBy.ID.

    Returns:
        The parsed response.
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
