import datetime
import functools
from http import HTTPStatus
from typing import Any, Callable, Dict, Optional, TypeVar, Union, cast

import httpx
from typing_extensions import Concatenate, ParamSpec

from ....credentials import HightouchCredentials
from ...client import AuthenticatedClient
from ...models.list_sync_order_by import ListSyncOrderBy
from ...models.list_sync_response_200 import ListSyncResponse200
from ...models.validate_error_json import ValidateErrorJSON
from ...types import UNSET, Response, Unset

C = ParamSpec("C")  # client function
T = ParamSpec("T")  # task function
R = TypeVar("R")  # The return type of the API function


def _wrap_request(
    client_fn: Callable[Concatenate[AuthenticatedClient, C], R]
) -> Callable[[Callable[C, R]], Callable[Concatenate[HightouchCredentials, C], R]]:
    def wrap(task_fn: Callable[T, R]) -> Callable[T, R]:
        @functools.wraps(task_fn)
        async def run(*args: T.args, **kwargs: T.kwargs) -> R:
            hightouch_credentials = None
            if "hightouch_credentials" in kwargs:
                hightouch_credentials = kwargs.pop("hightouch_credentials")
                input_args = args
            else:
                hightouch_credentials = args[0]
                input_args = args[1:]
            kwargs["client"] = hightouch_credentials.get_client()
            return await client_fn(*input_args, **kwargs)

        return run

    return wrap


def _get_kwargs(
    client: AuthenticatedClient,
    slug: Union[Unset, None, str] = UNSET,
    model_id: Union[Unset, None, float] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSyncOrderBy] = ListSyncOrderBy.ID,
) -> Dict[str, Any]:
    url = "{}/syncs".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["slug"] = slug

    params["modelId"] = model_id

    json_after: Union[Unset, None, str] = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat() if after else None

    params["after"] = json_after

    json_before: Union[Unset, None, str] = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat() if before else None

    params["before"] = json_before

    params["limit"] = limit

    json_order_by: Union[Unset, None, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value if order_by else None

    params["orderBy"] = json_order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, ListSyncResponse200, ValidateErrorJSON]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListSyncResponse200.from_dict(response.json())

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
) -> Response[Union[Any, ListSyncResponse200, ValidateErrorJSON]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    client: AuthenticatedClient,
    slug: Union[Unset, None, str] = UNSET,
    model_id: Union[Unset, None, float] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSyncOrderBy] = ListSyncOrderBy.ID,
) -> Response[Union[Any, ListSyncResponse200, ValidateErrorJSON]]:
    """List Syncs

     List all the syncs in the current workspace

    Args:
        slug (Union[Unset, None, str]):
        model_id (Union[Unset, None, float]):
        after (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSyncOrderBy]):  Default: ListSyncOrderBy.ID.

    Returns:
        Response[Union[Any, ListSyncResponse200, ValidateErrorJSON]]
    """

    kwargs = _get_kwargs(
        client=client,
        slug=slug,
        model_id=model_id,
        after=after,
        before=before,
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
    slug: Union[Unset, None, str] = UNSET,
    model_id: Union[Unset, None, float] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSyncOrderBy] = ListSyncOrderBy.ID,
) -> Optional[Union[Any, ListSyncResponse200, ValidateErrorJSON]]:
    """List Syncs

     List all the syncs in the current workspace

    Args:
        slug (Union[Unset, None, str]):
        model_id (Union[Unset, None, float]):
        after (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSyncOrderBy]):  Default: ListSyncOrderBy.ID.

    Returns:
        Response[Union[Any, ListSyncResponse200, ValidateErrorJSON]]
    """

    return sync_detailed(
        client=client,
        slug=slug,
        model_id=model_id,
        after=after,
        before=before,
        limit=limit,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    client: AuthenticatedClient,
    slug: Union[Unset, None, str] = UNSET,
    model_id: Union[Unset, None, float] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSyncOrderBy] = ListSyncOrderBy.ID,
) -> Response[Union[Any, ListSyncResponse200, ValidateErrorJSON]]:
    """List Syncs

     List all the syncs in the current workspace

    Args:
        slug (Union[Unset, None, str]):
        model_id (Union[Unset, None, float]):
        after (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSyncOrderBy]):  Default: ListSyncOrderBy.ID.

    Returns:
        Response[Union[Any, ListSyncResponse200, ValidateErrorJSON]]
    """

    kwargs = _get_kwargs(
        client=client,
        slug=slug,
        model_id=model_id,
        after=after,
        before=before,
        limit=limit,
        order_by=order_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    client: AuthenticatedClient,
    slug: Union[Unset, None, str] = UNSET,
    model_id: Union[Unset, None, float] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    order_by: Union[Unset, None, ListSyncOrderBy] = ListSyncOrderBy.ID,
) -> Optional[Union[Any, ListSyncResponse200, ValidateErrorJSON]]:
    """List Syncs

     List all the syncs in the current workspace

    Args:
        slug (Union[Unset, None, str]):
        model_id (Union[Unset, None, float]):
        after (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        limit (Union[Unset, None, float]):
        order_by (Union[Unset, None, ListSyncOrderBy]):  Default: ListSyncOrderBy.ID.

    Returns:
        Response[Union[Any, ListSyncResponse200, ValidateErrorJSON]]
    """

    return (
        await asyncio_detailed(
            client=client,
            slug=slug,
            model_id=model_id,
            after=after,
            before=before,
            limit=limit,
            order_by=order_by,
        )
    ).parsed
