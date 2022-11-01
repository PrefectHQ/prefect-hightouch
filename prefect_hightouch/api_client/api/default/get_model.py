from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.model import Model
from ...types import Response


def _get_kwargs(
    client: AuthenticatedClient,
    model_id: float,
) -> Dict[str, Any]:
    url = "{}/models/{modelId}".format(client.base_url, modelId=model_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Model]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Model.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Model]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    client: AuthenticatedClient,
    model_id: float,
) -> Response[Union[Any, Model]]:
    """Get Model

     Retrieve models from model ID

    Args:
        model_id (float):

    Returns:
        Response[Union[Any, Model]]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    client: AuthenticatedClient,
    model_id: float,
) -> Optional[Union[Any, Model]]:
    """Get Model

     Retrieve models from model ID

    Args:
        model_id (float):

    Returns:
        Response[Union[Any, Model]]
    """

    return sync_detailed(
        model_id=model_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    client: AuthenticatedClient,
    model_id: float,
) -> Response[Union[Any, Model]]:
    """Get Model

     Retrieve models from model ID

    Args:
        model_id (float):

    Returns:
        Response[Union[Any, Model]]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    client: AuthenticatedClient,
    model_id: float,
) -> Optional[Union[Any, Model]]:
    """Get Model

     Retrieve models from model ID

    Args:
        model_id (float):

    Returns:
        Response[Union[Any, Model]]
    """

    return (
        await asyncio_detailed(
            model_id=model_id,
            client=client,
        )
    ).parsed
