"""
This is a module containing tasks for interacting with:
Hightouch syncs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-10-27T03:04:31.819266

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client import api, models, types  # noqa
from prefect_hightouch.api_client.api.default.get_sync import asyncio as request


@task
async def get_sync(
    sync_id: float,
    hightouch_credentials: "HightouchCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieve sync from sync ID.

    Args:
        sync_id:
            Sync ID used in formatting the endpoint URL.
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.

    Returns:
        Upon success, a dict of the response. </br>- `id: str`</br>- `slug: str`</br>- `workspace_id: str`</br>- `created_at: str`</br>- `updated_at: str`</br>- `destination_id: str`</br>- `model_id: str`</br>- `configuration: Dict`</br>- `schedule: Dict`</br>- `status: "models.SyncStatus"`</br>- `disabled: bool`</br>- `last_run_at: str`</br>- `referenced_columns: List[str]`</br>- `primary_key: str`</br>

    <h4>API Endpoint:</h4>
    `/syncs/{sync_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 401 | Unauthorized. |
    | 404 | Not found. |
    """  # noqa
    client = hightouch_credentials.get_client()
    parsed = await request(
        sync_id=sync_id, hightouch_credentials=hightouch_credentials, client=client
    )
    return parsed
