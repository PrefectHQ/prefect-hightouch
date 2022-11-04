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
from ...models.trigger_run_input import TriggerRunInput
from ...models.trigger_run_output import TriggerRunOutput
from ...models.validate_error_json import ValidateErrorJSON
from ...types import UNSET, Response


def _get_kwargs(
    client: AuthenticatedClient,
    sync_id: str,
    json_body: TriggerRunInput,
) -> Dict[str, Any]:
    url = "{}/syncs/{syncId}/trigger".format(client.base_url, syncId=sync_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    kwargs = {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }

    if "json" in kwargs:
        kwargs["json"] = {k: v for k, v in kwargs["json"].items() if v != UNSET}
    return kwargs


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
    response.raise_for_status()

    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    client: AuthenticatedClient,
    sync_id: str,
    json_body: TriggerRunInput,
) -> Response[Union[Any, TriggerRunOutput, ValidateErrorJSON]]:
    """Trigger Sync

     Trigger a new run for the given sync.

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        client: An authenticated client.
        sync_id (str):
        json_body (TriggerRunInput): The input of a trigger action to run syncs

    Returns:
        The response.
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
    client: AuthenticatedClient,
    sync_id: str,
    json_body: TriggerRunInput,
) -> Optional[Union[Any, TriggerRunOutput, ValidateErrorJSON]]:
    """Trigger Sync

     Trigger a new run for the given sync.

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        client: An authenticated client.
        sync_id (str):
        json_body (TriggerRunInput): The input of a trigger action to run syncs

    Returns:
        The parsed response.
    """

    return sync_detailed(
        sync_id=sync_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    client: AuthenticatedClient,
    sync_id: str,
    json_body: TriggerRunInput,
) -> Response[Union[Any, TriggerRunOutput, ValidateErrorJSON]]:
    """Trigger Sync

     Trigger a new run for the given sync.

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        client: An authenticated client.
        sync_id (str):
        json_body (TriggerRunInput): The input of a trigger action to run syncs

    Returns:
        The response.
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
    client: AuthenticatedClient,
    sync_id: str,
    json_body: TriggerRunInput,
) -> Optional[Union[Any, TriggerRunOutput, ValidateErrorJSON]]:
    """Trigger Sync

     Trigger a new run for the given sync.

    If a run is already in progress, this queues a sync run that will get
    executed immediately after the current run completes.

    Args:
        client: An authenticated client.
        sync_id (str):
        json_body (TriggerRunInput): The input of a trigger action to run syncs

    Returns:
        The parsed response.
    """

    return (
        await asyncio_detailed(
            sync_id=sync_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
