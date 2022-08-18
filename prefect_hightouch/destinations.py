"""
This is a module containing tasks for interacting with:
Hightouch destinations
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-08-18T00:47:52.255768

from typing import TYPE_CHECKING, Any, Dict, List, Union  # noqa

from prefect import task

from prefect_hightouch.rest import HTTPMethod, _unpack_contents, execute_endpoint

if TYPE_CHECKING:
    from prefect_hightouch import HightouchCredentials


@task
async def get_destination(
    destination_id: str,
    hightouch_credentials: "HightouchCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a destination based on its Hightouch ID.

    Args:
        destination_id:
            Destination id used in formatting the endpoint URL.
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/destinations/{destination_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 401 | Unauthorized. |
    | 404 | Not found. |
    """  # noqa
    endpoint = f"/destinations/{destination_id}"  # noqa
    responses = {
        200: "Ok.",  # noqa
        401: "Unauthorized.",  # noqa
        404: "Not found.",  # noqa
    }

    params = {
        "destination_id": destination_id,
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
async def list_destination(
    hightouch_credentials: "HightouchCredentials",
    name: str = None,
    slug: str = None,
    limit: str = None,
    order_by: str = "id",
) -> Dict[str, Any]:
    """
    List the destinations in the user's workspace.

    Args:
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.
        name:
            Filter based on the destination's name.
        slug:
            Filter based on destination's slug.
        limit:
            Limit the number of returned destinations.
        order_by:
            Order the returned destinations.

    Returns:
        A dict of the response.

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
    endpoint = "/destinations"  # noqa

    responses = {
        200: "Ok.",  # noqa
        400: "Bad request.",  # noqa
        401: "Unauthorized.",  # noqa
        422: "Validation Failed.",  # noqa
    }

    params = {
        "name": name,
        "slug": slug,
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
