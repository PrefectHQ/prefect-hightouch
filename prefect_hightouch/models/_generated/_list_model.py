"""
This is a module containing tasks for interacting with:
Hightouch models
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-10-26T03:28:44.857791

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client.api.default.list_model import asyncio as request


@task
async def list_model(
    hightouch_credentials: "HightouchCredentials",
    name: Optional[str] = None,
    slug: Optional[str] = None,
    limit: Optional[str] = None,
    order_by: str = "id",
) -> Dict[str, Any]:  # pragma: no cover
    """
    List all the models in the current workspace.

    Args:
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.
        name:
            filter based on name.
        slug:
            filter based on slug.
        limit:
            limit the number of object it returns. Default is 100.
        order_by:
            specify the order.

    Returns:
        Upon success, a dict of the response. </br>- `data: List`</br>

    <h4>API Endpoint:</h4>
    `/models`

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
