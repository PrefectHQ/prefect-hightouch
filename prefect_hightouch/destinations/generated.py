"""
This is a module containing tasks, auto-generated from the Hightouch
REST schema, used for interacting with destinations.
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module is outdated
# rerun scripts/generate.py. To override the default generated output:
# 1. create a separate module and rewrite the class / function
# 2. import in `__init__.py`, under the `from .generated import *` line
# 3. hide the generated function in `docs/destinations.md` under `options`

# OpenAPI spec: swagger.yaml
# Updated at: 2022-11-01T00:16:53.461454


from prefect import task

from prefect_hightouch.api_client import types
from prefect_hightouch.api_client.api import _execute_endpoint
from prefect_hightouch.api_client.api.default.get_destination import (
    asyncio as _get_destination_endpoint,
)
from prefect_hightouch.api_client.api.default.list_destination import (
    asyncio as _list_destination_endpoint,
)


@task
@_execute_endpoint(_list_destination_endpoint)
async def list_destination(*args, **kwargs) -> types.Response:  # pragma: no cover
    """
    List the destinations in the user's workspace.

    Args:
        hightouch_credentials ("HightouchCredentials"):
            Credentials to use for authentication with Hightouch.
        name (Optional[str]):
            Filter based on the destination's name.
        slug (Optional[str]):
            Filter based on destination's slug.
        limit (Optional[str]):
            Limit the number of returned destinations.
        order_by (str):
            Order the returned destinations.

    Returns:
        A Response; use the `parsed` attribute to resolve data as models.

    <h4>API Endpoint:</h4>
    `/destinations`

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
@_execute_endpoint(_get_destination_endpoint)
async def get_destination(*args, **kwargs) -> types.Response:  # pragma: no cover
    """
    Retrieve a destination based on its Hightouch ID.

    Args:
        hightouch_credentials ("HightouchCredentials"):
            Credentials to use for authentication with Hightouch.
        destination_id (str):
            The destination's ID.

    Returns:
        A Response; use the `parsed` attribute to resolve data as models.

    <h4>API Endpoint:</h4>
    `/destinations/{destination_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 401 | Unauthorized. |
    | 404 | Not found. |
    """  # noqa
    ...
