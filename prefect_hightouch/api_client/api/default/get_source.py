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
from ...models.source import Source
from ...models.validate_error_json import ValidateErrorJSON
from ...types import UNSET, Response


def _get_kwargs(
    client: AuthenticatedClient,
    source_id: float,
) -> Dict[str, Any]:
    url = "{}/sources/{sourceId}".format(client.base_url, sourceId=source_id)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, Source, ValidateErrorJSON]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Source.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ValidateErrorJSON.from_dict(response.json())

        return response_422
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, Source, ValidateErrorJSON]]:
    response.raise_for_status()

    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    client: AuthenticatedClient,
    source_id: float,
) -> Response[Union[Any, Source, ValidateErrorJSON]]:
    """Get Source

     Retrieve source from source ID

    Args:
        client: An authenticated client.
        source_id (float):

    Returns:
        The response.
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    client: AuthenticatedClient,
    source_id: float,
) -> Optional[Union[Any, Source, ValidateErrorJSON]]:
    """Get Source

     Retrieve source from source ID

    Args:
        client: An authenticated client.
        source_id (float):

    Returns:
        The parsed response.
    """

    return sync_detailed(
        source_id=source_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    client: AuthenticatedClient,
    source_id: float,
) -> Response[Union[Any, Source, ValidateErrorJSON]]:
    """Get Source

     Retrieve source from source ID

    Args:
        client: An authenticated client.
        source_id (float):

    Returns:
        The response.
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    client: AuthenticatedClient,
    source_id: float,
) -> Optional[Union[Any, Source, ValidateErrorJSON]]:
    """Get Source

     Retrieve source from source ID

    Args:
        client: An authenticated client.
        source_id (float):

    Returns:
        The parsed response.
    """

    return (
        await asyncio_detailed(
            source_id=source_id,
            client=client,
        )
    ).parsed
