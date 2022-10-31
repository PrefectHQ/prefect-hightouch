"""
This is a module containing tasks for interacting with:
Hightouch destinations
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-10-31T19:39:31.383595


from prefect import task

from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client import types
from prefect_hightouch.api_client.api.default.list_destination import _wrap_request
from prefect_hightouch.api_client.api.default.list_destination import (
    asyncio_detailed as request,
)


@task
@_wrap_request(request)
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
    return await request(*args, **kwargs)


@task
@_wrap_request(request)
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
    return await request(*args, **kwargs)
