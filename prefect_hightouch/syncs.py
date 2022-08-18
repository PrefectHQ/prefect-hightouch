"""
This is a module containing tasks for interacting with:
Hightouch syncs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-08-18T00:47:52.259575

from typing import TYPE_CHECKING, Any, Dict, List, Union  # noqa

from prefect import task

from prefect_hightouch.rest import HTTPMethod, _unpack_contents, execute_endpoint

if TYPE_CHECKING:
    from prefect_hightouch import HightouchCredentials


@task
async def get_sync(
    sync_id: str,
    hightouch_credentials: "HightouchCredentials",
) -> Dict[str, Any]:
    """
    Retrieve sync from sync ID.

    Args:
        sync_id:
            Sync id used in formatting the endpoint URL.
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/syncs/{sync_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 401 | Unauthorized. |
    | 404 | Not found. |
    """  # noqa
    endpoint = f"/syncs/{sync_id}"  # noqa
    responses = {
        200: "Ok.",  # noqa
        401: "Unauthorized.",  # noqa
        404: "Not found.",  # noqa
    }

    params = {
        "sync_id": sync_id,
    }

    response = await execute_endpoint.fn(
        endpoint,
        hightouch_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def list_sync(
    hightouch_credentials: "HightouchCredentials",
    slug: str = None,
    model_id: str = None,
    after: str = None,
    before: str = None,
    limit: str = None,
    order_by: str = "id",
) -> Dict[str, Any]:
    """
    List all the syncs in the current workspace.

    Args:
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.
        slug:
            filter based on slug.
        model_id:
            filter based on modelId.
        after:
            select syncs that were run after given time.
        before:
            select syncs that were run before given time.
        limit:
            limit the number of object it returns. Default is 100.
        order_by:
            specify the order.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/syncs`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 422 | Validation Failed. |
    """  # noqa
    endpoint = "/syncs"  # noqa

    responses = {
        200: "Ok.",  # noqa
        400: "Bad request.",  # noqa
        401: "Unauthorized.",  # noqa
        422: "Validation Failed.",  # noqa
    }

    params = {
        "slug": slug,
        "model_id": model_id,
        "after": after,
        "before": before,
        "limit": limit,
        "order_by": order_by,
    }

    response = await execute_endpoint.fn(
        endpoint,
        hightouch_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def list_sync_runs(
    sync_id: str,
    hightouch_credentials: "HightouchCredentials",
    run_id: str = None,
    limit: str = None,
    offset: str = None,
    after: str = None,
    before: str = None,
    within: str = None,
    order_by: str = "id",
) -> Dict[str, Any]:
    """
    List all sync runs under a sync.

    Args:
        sync_id:
            Sync id used in formatting the endpoint URL.
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.
        run_id:
            query for specific run id.
        limit:
            limit the number of object it returns. Default is 5.
        offset:
            setting offset from result(for pagination).
        after:
            select sync runs that are started after given timestamp.
        before:
            select sync runs that are started before certain timestamp.
        within:
            select sync runs that are started within last given minutes.
        order_by:
            specify the order.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/syncs/{sync_id}/runs`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 422 | Validation Failed. |
    """  # noqa
    endpoint = f"/syncs/{sync_id}/runs"  # noqa
    responses = {
        200: "Ok.",  # noqa
        400: "Bad request.",  # noqa
        401: "Unauthorized.",  # noqa
        422: "Validation Failed.",  # noqa
    }

    params = {
        "sync_id": sync_id,
        "run_id": run_id,
        "limit": limit,
        "offset": offset,
        "after": after,
        "before": before,
        "within": within,
        "order_by": order_by,
    }

    response = await execute_endpoint.fn(
        endpoint,
        hightouch_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def trigger_run(
    sync_id: str,
    hightouch_credentials: "HightouchCredentials",
    full_resync: bool = "false",
) -> Dict[str, Any]:
    """
    Trigger a new run for the given sync.  If a run is already in progress, this
    queues a sync run that will get executed immediately after the current run
    completes.

    Args:
        sync_id:
            Sync id used in formatting the endpoint URL.
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.
        full_resync:
            Whether to resync all the rows in the query (i.e. ignoring previously
            synced rows).

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/syncs/{sync_id}/trigger`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 422 | Validation Failed. |
    """  # noqa
    endpoint = f"/syncs/{sync_id}/trigger"  # noqa
    responses = {
        200: "Ok.",  # noqa
        400: "Bad request.",  # noqa
        401: "Unauthorized.",  # noqa
        422: "Validation Failed.",  # noqa
    }

    params = {
        "sync_id": sync_id,
    }

    json_payload = {
        "full_resync": full_resync,
    }

    response = await execute_endpoint.fn(
        endpoint,
        hightouch_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        json=json_payload,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def trigger_run_custom(
    hightouch_credentials: "HightouchCredentials",
    sync_slug: str = None,
    sync_id: str = None,
    full_resync: bool = "false",
) -> Dict[str, Any]:
    """
    Trigger a new run globally based on sync id or sync slug  If a run is already in
    progress, this queues a sync run that will get executed immediately after
    the current run completes.

    Args:
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.
        sync_slug:
            Trigger run based on sync slug.
        sync_id:
            Trigger run based on sync id.
        full_resync:
            Whether to resync all the rows in the query (i.e. ignoring previously
            synced rows).

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/syncs/trigger`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 422 | Validation Failed. |
    """  # noqa
    endpoint = "/syncs/trigger"  # noqa

    responses = {
        200: "Ok.",  # noqa
        400: "Bad request.",  # noqa
        401: "Unauthorized.",  # noqa
        422: "Validation Failed.",  # noqa
    }

    json_payload = {
        "sync_slug": sync_slug,
        "sync_id": sync_id,
        "full_resync": full_resync,
    }

    response = await execute_endpoint.fn(
        endpoint,
        hightouch_credentials,
        http_method=HTTPMethod.POST,
        json=json_payload,
    )

    contents = _unpack_contents(response, responses)
    return contents
