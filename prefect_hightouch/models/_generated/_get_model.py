"""
This is a module containing tasks for interacting with:
Hightouch models
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-10-27T03:04:31.813338

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client import api, models, types  # noqa
from prefect_hightouch.api_client.api.default.get_model import asyncio as request


@task
async def get_model(
    model_id: float,
    hightouch_credentials: "HightouchCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieve models from model ID.

    Args:
        model_id:
            Model ID used in formatting the endpoint URL.
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.

    Returns:
        Upon success, a dict of the response. </br>- `id: str`</br>- `name: str`</br>- `slug: str`</br>- `workspace_id: str`</br>- `primary_key: str`</br>- `created_at: str`</br>- `updated_at: str`</br>- `source_id: str`</br>- `query_type: str`</br>- `tags: Dict`</br>- `is_schema: bool`</br>- `syncs: List[str]`</br>- `visual: Dict`</br>- `custom: Dict`</br>- `table: Dict`</br>- `dbt: Dict`</br>- `raw: Dict`</br>

    <h4>API Endpoint:</h4>
    `/models/{model_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 401 | Unauthorized. |
    | 404 | Not found. |
    """  # noqa
    client = hightouch_credentials.get_client()
    parsed = await request(
        model_id=model_id, hightouch_credentials=hightouch_credentials, client=client
    )
    return parsed
