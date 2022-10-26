from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.trigger_run_input import TriggerRunInput
from ...models.trigger_run_output import TriggerRunOutput
from ...models.validate_error_json import ValidateErrorJSON
from ...types import Response


def _get_kwargs(
    sync_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TriggerRunInput,
) -> Dict[str, Any]:
    url = "{}/syncs/{syncId}/trigger".format(client.base_url, syncId=sync_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, TriggerRunOutput, ValidateErrorJSON]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TriggerRunOutput.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ValidateErrorJSON.from_dict(response.json())

        return response_422
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, TriggerRunOutput, ValidateErrorJSON]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    sync_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TriggerRunInput,
) -> Response[Union[Any, TriggerRunOutput, ValidateErrorJSON]]:
    """Trigger Sync

     Trigger a new run for the given sync.

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        sync_id (str):
        json_body (TriggerRunInput): The input of a trigger action to run syncs

    Returns:
        Response[Union[Any, TriggerRunOutput, ValidateErrorJSON]]
    """

    kwargs = _get_kwargs(
        sync_id=sync_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    sync_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TriggerRunInput,
) -> Optional[Union[Any, TriggerRunOutput, ValidateErrorJSON]]:
    """Trigger Sync

     Trigger a new run for the given sync.

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        sync_id (str):
        json_body (TriggerRunInput): The input of a trigger action to run syncs

    Returns:
        Response[Union[Any, TriggerRunOutput, ValidateErrorJSON]]
    """

    return sync_detailed(
        sync_id=sync_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    sync_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TriggerRunInput,
) -> Response[Union[Any, TriggerRunOutput, ValidateErrorJSON]]:
    """Trigger Sync

     Trigger a new run for the given sync.

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        sync_id (str):
        json_body (TriggerRunInput): The input of a trigger action to run syncs

    Returns:
        Response[Union[Any, TriggerRunOutput, ValidateErrorJSON]]
    """

    kwargs = _get_kwargs(
        sync_id=sync_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    sync_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TriggerRunInput,
) -> Optional[Union[Any, TriggerRunOutput, ValidateErrorJSON]]:
    """Trigger Sync

     Trigger a new run for the given sync.

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        sync_id (str):
        json_body (TriggerRunInput): The input of a trigger action to run syncs

    Returns:
        Response[Union[Any, TriggerRunOutput, ValidateErrorJSON]]
    """

    return (
        await asyncio_detailed(
            sync_id=sync_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
