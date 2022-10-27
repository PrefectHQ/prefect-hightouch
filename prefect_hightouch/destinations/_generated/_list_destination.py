"""
This is a module containing tasks for interacting with:
Hightouch destinations
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-10-27T03:04:31.808203

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client import api, models, types  # noqa
from prefect_hightouch.api_client.api.default.list_destination import asyncio as request


@task
async def list_destination(
    hightouch_credentials: "HightouchCredentials",
    name: Union[types.Unset, None, str] = types.UNSET,
    slug: Union[types.Unset, None, str] = types.UNSET,
    limit: Union[types.Unset, None, float] = types.UNSET,
    order_by: Union[
        types.Unset, None, models.list_destination_order_by.ListDestinationOrderBy
    ] = id,
) -> Dict[str, Any]:  # pragma: no cover
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
        Upon success, a dict of the response. </br>- `data: List`</br>

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
    client = hightouch_credentials.get_client()
    parsed = await request(
        hightouch_credentials=hightouch_credentials,
        name=name,
        slug=slug,
        limit=limit,
        order_by=order_by,
        client=client,
    )
    return parsed
