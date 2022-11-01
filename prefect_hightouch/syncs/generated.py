"""
This is a module containing tasks, auto-generated from the Hightouch
REST schema, used for interacting with syncs.
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module is outdated
# rerun scripts/generate.py. To override the default generated output:
# 1. create a separate module and rewrite the class / function
# 2. import in `__init__.py`, under the `from .generated import *` line
# 3. hide the generated function in `docs/syncs.md` under `options`

# OpenAPI spec: swagger.yaml
# Updated at: 2022-11-01T00:16:53.466238


from prefect import task

from prefect_hightouch.api_client import types
from prefect_hightouch.api_client.api import _execute_endpoint
from prefect_hightouch.api_client.api.default.get_sync import (
    asyncio as _get_sync_endpoint,
)
from prefect_hightouch.api_client.api.default.list_sync import (
    asyncio as _list_sync_endpoint,
)
from prefect_hightouch.api_client.api.default.list_sync_runs import (
    asyncio as _list_sync_runs_endpoint,
)
from prefect_hightouch.api_client.api.default.trigger_run import (
    asyncio as _trigger_run_endpoint,
)
from prefect_hightouch.api_client.api.default.trigger_run_custom import (
    asyncio as _trigger_run_custom_endpoint,
)


@task
@_execute_endpoint(_list_sync_endpoint)
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
    ...


@task
@_execute_endpoint(_trigger_run_custom_endpoint)
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
    ...


@task
@_execute_endpoint(_get_sync_endpoint)
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
    ...


@task
@_execute_endpoint(_list_sync_runs_endpoint)
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
    ...


@task
@_execute_endpoint(_trigger_run_endpoint)
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
    ...
