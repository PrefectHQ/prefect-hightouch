from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.sync import Sync
from ...types import Response


def _get_kwargs(
    sync_id: float,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/syncs/{syncId}".format(client.base_url, syncId=sync_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Sync]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Sync.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Sync]]:
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
) -> Response[Union[Any, Sync]]:
    """Get Sync

     Retrieve sync from sync ID

    Args:
        sync_id (float):

    Returns:
        Response[Union[Any, Sync]]
    """

    kwargs = _get_kwargs(
        sync_id=sync_id,
        client=client,
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
) -> Optional[Union[Any, Sync]]:
    """Get Sync

     Retrieve sync from sync ID

    Args:
        sync_id (float):

    Returns:
        Response[Union[Any, Sync]]
    """

    return sync_detailed(
        sync_id=sync_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sync_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Sync]]:
    """Get Sync

     Retrieve sync from sync ID

    Args:
        sync_id (float):

    Returns:
        Response[Union[Any, Sync]]
    """

    kwargs = _get_kwargs(
        sync_id=sync_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    sync_id: float,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Sync]]:
    """Get Sync

     Retrieve sync from sync ID

    Args:
        sync_id (float):

    Returns:
        Response[Union[Any, Sync]]
    """

    return (
        await asyncio_detailed(
            sync_id=sync_id,
            client=client,
        )
    ).parsed
