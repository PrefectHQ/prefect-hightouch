from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from prefect import task

from ....credentials import HightouchCredentials
from ...client import AuthenticatedClient
from ...models.trigger_run_custom_input import TriggerRunCustomInput
from ...models.trigger_run_output import TriggerRunOutput
from ...models.validate_error_json import ValidateErrorJSON
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: TriggerRunCustomInput,
) -> Dict[str, Any]:
    url = "{}/syncs/trigger".format(client.base_url)

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
) -> Optional[
    Union[Any, Union[TriggerRunOutput, ValidateErrorJSON], ValidateErrorJSON]
]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union[TriggerRunOutput, ValidateErrorJSON]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = TriggerRunOutput.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = ValidateErrorJSON.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[
    Union[Any, Union[TriggerRunOutput, ValidateErrorJSON], ValidateErrorJSON]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: TriggerRunCustomInput,
) -> Response[
    Union[Any, Union[TriggerRunOutput, ValidateErrorJSON], ValidateErrorJSON]
]:
    """Trigger Sync From ID or Slug

     Trigger a new run globally based on sync id or sync slug

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        json_body (TriggerRunCustomInput): The input of a trigger action to run syncs based on
            sync ID, slug or other filters

    Returns:
        Response[Union[Any, Union[TriggerRunOutput, ValidateErrorJSON], ValidateErrorJSON]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: TriggerRunCustomInput,
) -> Optional[
    Union[Any, Union[TriggerRunOutput, ValidateErrorJSON], ValidateErrorJSON]
]:
    """Trigger Sync From ID or Slug

     Trigger a new run globally based on sync id or sync slug

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        json_body (TriggerRunCustomInput): The input of a trigger action to run syncs based on
            sync ID, slug or other filters

    Returns:
        Response[Union[Any, Union[TriggerRunOutput, ValidateErrorJSON], ValidateErrorJSON]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: TriggerRunCustomInput,
) -> Response[
    Union[Any, Union[TriggerRunOutput, ValidateErrorJSON], ValidateErrorJSON]
]:
    """Trigger Sync From ID or Slug

     Trigger a new run globally based on sync id or sync slug

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        json_body (TriggerRunCustomInput): The input of a trigger action to run syncs based on
            sync ID, slug or other filters

    Returns:
        Response[Union[Any, Union[TriggerRunOutput, ValidateErrorJSON], ValidateErrorJSON]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: TriggerRunCustomInput,
) -> Optional[
    Union[Any, Union[TriggerRunOutput, ValidateErrorJSON], ValidateErrorJSON]
]:
    """Trigger Sync From ID or Slug

     Trigger a new run globally based on sync id or sync slug

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        json_body (TriggerRunCustomInput): The input of a trigger action to run syncs based on
            sync ID, slug or other filters

    Returns:
        Response[Union[Any, Union[TriggerRunOutput, ValidateErrorJSON], ValidateErrorJSON]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed


@task(name="TriggerRunCustom")
async def asyncio_task(
    hightouch_credentials: HightouchCredentials,
    json_body: TriggerRunCustomInput,
) -> Optional[
    Union[Any, Union[TriggerRunOutput, ValidateErrorJSON], ValidateErrorJSON]
]:
    """Trigger Sync From ID or Slug

     Trigger a new run globally based on sync id or sync slug

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        json_body (TriggerRunCustomInput): The input of a trigger action to run syncs based on
            sync ID, slug or other filters

    Returns:
        Response[Union[Any, Union[TriggerRunOutput, ValidateErrorJSON], ValidateErrorJSON]]
    """

    client = hightouch_credentials.get_client()
    return await asyncio(
        client=client,
        json_body=json_body,
    )
