from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.destination import Destination
from ...types import Response


def _get_kwargs(
    destination_id: float,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/destinations/{destinationId}".format(
        client.base_url, destinationId=destination_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Destination]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Destination.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Destination]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    destination_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Destination]]:
    """Get Destination

     Retrieve a destination based on its Hightouch ID

    Args:
        destination_id (float):

    Returns:
        Response[Union[Any, Destination]]
    """

    kwargs = _get_kwargs(
        destination_id=destination_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    destination_id: float,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Destination]]:
    """Get Destination

     Retrieve a destination based on its Hightouch ID

    Args:
        destination_id (float):

    Returns:
        Response[Union[Any, Destination]]
    """

    return sync_detailed(
        destination_id=destination_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    destination_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Destination]]:
    """Get Destination

     Retrieve a destination based on its Hightouch ID

    Args:
        destination_id (float):

    Returns:
        Response[Union[Any, Destination]]
    """

    kwargs = _get_kwargs(
        destination_id=destination_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    destination_id: float,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Destination]]:
    """Get Destination

     Retrieve a destination based on its Hightouch ID

    Args:
        destination_id (float):

    Returns:
        Response[Union[Any, Destination]]
    """

    return (
        await asyncio_detailed(
            destination_id=destination_id,
            client=client,
        )
    ).parsed
