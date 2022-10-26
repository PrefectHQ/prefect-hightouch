"""
This is a module containing tasks for interacting with:
Hightouch destinations
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-10-26T03:28:44.857354

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client.api.default.get_destination import asyncio as request


@task
async def get_destination(
    destination_id: str,
    hightouch_credentials: "HightouchCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieve a destination based on its Hightouch ID.

    Args:
        destination_id:
            Destination ID used in formatting the endpoint URL.
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.

    Returns:
        Upon success, a dict of the response. </br>- `id: str`</br>- `name: str`</br>- `slug: str`</br>- `workspace_id: str`</br>- `created_at: str`</br>- `updated_at: str`</br>- `type: str`</br>- `configuration: Dict`</br>- `syncs: List[str]`</br>

    <h4>API Endpoint:</h4>
    `/destinations/{destination_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 401 | Unauthorized. |
    | 404 | Not found. |
    """  # noqa
    client = hightouch_credentials.get_client()
    parsed = await request(
        destination_id=destination_id,
        hightouch_credentials=hightouch_credentials,
        client=client,
    )
    return parsed
