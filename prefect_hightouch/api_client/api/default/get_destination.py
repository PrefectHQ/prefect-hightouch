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
from ...models.destination import Destination
from ...types import UNSET, Response


def _get_kwargs(
    client: AuthenticatedClient,
    destination_id: float,
) -> Dict[str, Any]:
    url = "{}/destinations/{destinationId}".format(
        client.base_url, destinationId=destination_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    kwargs = {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }

    if "json" in kwargs:
        kwargs["json"] = {k: v for k, v in kwargs["json"].items() if v != UNSET}
    return kwargs


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
    response.raise_for_status()

    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    client: AuthenticatedClient,
    destination_id: float,
) -> Response[Union[Any, Destination]]:
    """Get Destination

     Retrieve a destination based on its Hightouch ID

    Args:
        client: An authenticated client.
        destination_id (float):

    Returns:
        The response.
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
    client: AuthenticatedClient,
    destination_id: float,
) -> Optional[Union[Any, Destination]]:
    """Get Destination

     Retrieve a destination based on its Hightouch ID

    Args:
        client: An authenticated client.
        destination_id (float):

    Returns:
        The parsed response.
    """

    return sync_detailed(
        destination_id=destination_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    client: AuthenticatedClient,
    destination_id: float,
) -> Response[Union[Any, Destination]]:
    """Get Destination

     Retrieve a destination based on its Hightouch ID

    Args:
        client: An authenticated client.
        destination_id (float):

    Returns:
        The response.
    """

    kwargs = _get_kwargs(
        destination_id=destination_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    client: AuthenticatedClient,
    destination_id: float,
) -> Optional[Union[Any, Destination]]:
    """Get Destination

     Retrieve a destination based on its Hightouch ID

    Args:
        client: An authenticated client.
        destination_id (float):

    Returns:
        The parsed response.
    """

    return (
        await asyncio_detailed(
            destination_id=destination_id,
            client=client,
        )
    ).parsed
