"""
This is a module containing tasks for interacting with:
Hightouch sources
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-10-26T03:28:44.859424

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client.api.default.get_source import asyncio as request


@task
async def get_source(
    source_id: str,
    hightouch_credentials: "HightouchCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieve source from source ID.

    Args:
        source_id:
            Source ID used in formatting the endpoint URL.
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.

    Returns:
        Upon success, a dict of the response. </br>- `id: str`</br>- `name: str`</br>- `slug: str`</br>- `workspace_id: str`</br>- `created_at: str`</br>- `updated_at: str`</br>- `configuration: Dict`</br>- `type: str`</br>

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
    client = hightouch_credentials.get_client()
    parsed = await request(
        source_id=source_id, hightouch_credentials=hightouch_credentials, client=client
    )
    return parsed
