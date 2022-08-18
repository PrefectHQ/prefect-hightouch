"""
This is a module containing tasks for interacting with:
Hightouch sources
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-08-18T00:47:52.258844

from typing import TYPE_CHECKING, Any, Dict, List, Union  # noqa

from prefect import task

from prefect_hightouch.rest import HTTPMethod, _unpack_contents, execute_endpoint

if TYPE_CHECKING:
    from prefect_hightouch import HightouchCredentials


@task
async def get_source(
    source_id: str,
    hightouch_credentials: "HightouchCredentials",
) -> Dict[str, Any]:
    """
    Retrieve source from source ID.

    Args:
        source_id:
            Source id used in formatting the endpoint URL.
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.

    Returns:
        A dict of the response.

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
    endpoint = f"/sources/{source_id}"  # noqa
    responses = {
        200: "Ok.",  # noqa
        401: "Unauthorized.",  # noqa
        404: "Not found.",  # noqa
        422: "Validation Failed.",  # noqa
    }

    params = {
        "source_id": source_id,
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
async def list_source(
    hightouch_credentials: "HightouchCredentials",
    name: str = None,
    slug: str = None,
    limit: str = None,
    order_by: str = "id",
) -> Dict[str, Any]:
    """
    List all the sources in the current workspace.

    Args:
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.
        name:
            filter based on name.
        slug:
            filter based on slug.
        limit:
            limit the number of object it returns.
        order_by:
            specify the order.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/sources`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    """  # noqa
    endpoint = "/sources"  # noqa

    responses = {
        200: "Ok.",  # noqa
        400: "Bad request.",  # noqa
        401: "Unauthorized.",  # noqa
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
