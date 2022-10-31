"""
This is a module containing tasks for interacting with:
Hightouch syncs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-10-31T19:39:31.389296


from prefect import task

from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client import types
from prefect_hightouch.api_client.api.default.list_sync import _wrap_request
from prefect_hightouch.api_client.api.default.list_sync import (
    asyncio_detailed as request,
)


@task
@_wrap_request(request)
async def list_sync(*args, **kwargs) -> types.Response:  # pragma: no cover
    """
    List all the syncs in the current workspace.

    Args:
        hightouch_credentials ("HightouchCredentials"):
            Credentials to use for authentication with Hightouch.
        slug (Optional[str]):
            Filter based on slug.
        model_id (Optional[str]):
            Filter based on modelId.
        after (Optional[str]):
            Select syncs that were run after given time.
        before (Optional[str]):
            Select syncs that were run before given time.
        limit (Optional[str]):
            Limit the number of object it returns. Default is 100.
        order_by (str):
            Specify the order.

    Returns:
        A Response; use the `parsed` attribute to resolve data as models.

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
    return await request(*args, **kwargs)


@task
@_wrap_request(request)
async def trigger_run_custom(*args, **kwargs) -> types.Response:  # pragma: no cover
    """
    Trigger a new run globally based on sync id or sync slug  If a run is already in
    progress, this queues a sync run that will get executed immediately after
    the current run completes.

    Args:
        hightouch_credentials ("HightouchCredentials"):
            Credentials to use for authentication with Hightouch.
        sync_slug (Optional[str]):
            Trigger run based on sync slug.
        sync_id (Optional[str]):
            Trigger run based on sync id.
        full_resync (bool):
            Whether to resync all the rows in the query (i.e. ignoring previously
            synced rows).

    Returns:
        A Response; use the `parsed` attribute to resolve data as models.

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
    return await request(*args, **kwargs)


@task
@_wrap_request(request)
async def get_sync(*args, **kwargs) -> types.Response:  # pragma: no cover
    """
    Retrieve sync from sync ID.

    Args:
        hightouch_credentials ("HightouchCredentials"):
            Credentials to use for authentication with Hightouch.
        sync_id (str):
            The id of the sync.

    Returns:
        A Response; use the `parsed` attribute to resolve data as models.

    <h4>API Endpoint:</h4>
    `/syncs/{sync_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 401 | Unauthorized. |
    | 404 | Not found. |
    """  # noqa
    return await request(*args, **kwargs)


@task
@_wrap_request(request)
async def list_sync_runs(*args, **kwargs) -> types.Response:  # pragma: no cover
    """
    List all sync runs under a sync.

    Args:
        hightouch_credentials ("HightouchCredentials"):
            Credentials to use for authentication with Hightouch.
        sync_id (str):

        run_id (Optional[str]):
            Query for specific run id.
        limit (Optional[str]):
            Limit the number of object it returns. Default is 5.
        offset (Optional[str]):
            Setting offset from result(for pagination).
        after (Optional[str]):
            Select sync runs that are started after given timestamp.
        before (Optional[str]):
            Select sync runs that are started before certain timestamp.
        within (Optional[str]):
            Select sync runs that are started within last given minutes.
        order_by (str):
            Specify the order.

    Returns:
        A Response; use the `parsed` attribute to resolve data as models.

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
    return await request(*args, **kwargs)


@task
@_wrap_request(request)
async def trigger_run(*args, **kwargs) -> types.Response:  # pragma: no cover
    """
    Trigger a new run for the given sync.  If a run is already in progress, this
    queues a sync run that will get executed immediately after the current run
    completes.

    Args:
        hightouch_credentials ("HightouchCredentials"):
            Credentials to use for authentication with Hightouch.
        sync_id (str):
            The id of the sync to trigger a run.
        full_resync (bool):
            Whether to resync all the rows in the query (i.e. ignoring previously
            synced rows).

    Returns:
        A Response; use the `parsed` attribute to resolve data as models.

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
    return await request(*args, **kwargs)
