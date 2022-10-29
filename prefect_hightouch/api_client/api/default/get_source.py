from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from prefect import task

from ....credentials import HightouchCredentials
from ...client import AuthenticatedClient
from ...models.source import Source
from ...models.validate_error_json import ValidateErrorJSON
from ...types import Response


def _get_kwargs(
    source_id: float,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/sources/{sourceId}".format(client.base_url, sourceId=source_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, Source, ValidateErrorJSON]]:
    if response.status_code == 200:
        response_200 = Source.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 422:
        response_422 = ValidateErrorJSON.from_dict(response.json())

        return response_422
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, Source, ValidateErrorJSON]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    source_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Source, ValidateErrorJSON]]:
    """Get Source

     Retrieve source from source ID

    Args:
        source_id (float):

    Returns:
        Response[Union[Any, Source, ValidateErrorJSON]]
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
    source_id: float,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Source, ValidateErrorJSON]]:
    """Get Source

     Retrieve source from source ID

    Args:
        source_id (float):

    Returns:
        Response[Union[Any, Source, ValidateErrorJSON]]
    """

    return sync_detailed(
        source_id=source_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    source_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Source, ValidateErrorJSON]]:
    """Get Source

     Retrieve source from source ID

    Args:
        source_id (float):

    Returns:
        Response[Union[Any, Source, ValidateErrorJSON]]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    source_id: float,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Source, ValidateErrorJSON]]:
    """Get Source

     Retrieve source from source ID

    Args:
        source_id (float):

    Returns:
        Response[Union[Any, Source, ValidateErrorJSON]]
    """

    return (
        await asyncio_detailed(
            source_id=source_id,
            client=client,
        )
    ).parsed


@task(name="GetSource")
async def asyncio_task(
    hightouch_credentials: HightouchCredentials,
    source_id: float,
) -> Optional[Union[Any, Source, ValidateErrorJSON]]:
    """Get Source

     Retrieve source from source ID

    Args:
        source_id (float):

    Returns:
        Response[Union[Any, Source, ValidateErrorJSON]]
    """

    client = hightouch_credentials.get_client()
    return await asyncio(
        source_id=source_id,
        client=client,
    )
