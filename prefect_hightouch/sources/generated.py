"""
This is a module containing tasks, auto-generated from the Hightouch
REST schema, used for interacting with sources.
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module is outdated
# rerun scripts/generate.py. To override the default generated output:
# 1. create a separate module and rewrite the class / function
# 2. import in `__init__.py`, under the `from .generated import *` line
# 3. hide the generated function in `docs/sources.md` under `options`

# OpenAPI spec: swagger.yaml
# Updated at: 2022-11-01T00:16:53.465313


from prefect import task

from prefect_hightouch.api_client import types
from prefect_hightouch.api_client.api import _execute_endpoint
from prefect_hightouch.api_client.api.default.get_source import (
    asyncio as _get_source_endpoint,
)
from prefect_hightouch.api_client.api.default.list_source import (
    asyncio as _list_source_endpoint,
)


@task
@_execute_endpoint(_list_source_endpoint)
async def list_source(*args, **kwargs) -> types.Response:  # pragma: no cover
    """
    List all the sources in the current workspace.

    Args:
        hightouch_credentials ("HightouchCredentials"):
            Credentials to use for authentication with Hightouch.
        name (Optional[str]):
            Filter based on name.
        slug (Optional[str]):
            Filter based on slug.
        limit (Optional[str]):
            Limit the number of object it returns.
        order_by (str):
            Specify the order.

    Returns:
        A Response; use the `parsed` attribute to resolve data as models.

    <h4>API Endpoint:</h4>
    `/sources`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    """  # noqa
    ...


@task
@_execute_endpoint(_get_source_endpoint)
async def get_source(*args, **kwargs) -> types.Response:  # pragma: no cover
    """
    Retrieve source from source ID.

    Args:
        hightouch_credentials ("HightouchCredentials"):
            Credentials to use for authentication with Hightouch.
        source_id (str):
            The id of the source.

    Returns:
        A Response; use the `parsed` attribute to resolve data as models.

    <h4>API Endpoint:</h4>
    `/sources/{source_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 401 | Unauthorized. |
    | 404 | Not found. |
    | 422 | Validation Failed. |
    """  # noqa
    ...
