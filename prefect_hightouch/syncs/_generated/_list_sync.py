"""
This is a module containing tasks for interacting with:
Hightouch syncs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: swagger.yaml
# Updated at: 2022-10-26T03:21:11.835765

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client.api.default.get_sync import asyncio


@task
async def list_sync(
    hightouch_credentials: "HightouchCredentials",
    slug: Optional[str] = None,
    model_id: Optional[str] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    limit: Optional[str] = None,
    order_by: str = "id",
) -> Dict[str, Any]:  # pragma: no cover
    """
    List all the syncs in the current workspace.

    Args:
        hightouch_credentials:
            Credentials to use for authentication with Hightouch.
        slug:
            filter based on slug.
        model_id:
            filter based on modelId.
        after:
            select syncs that were run after given time.
        before:
            select syncs that were run before given time.
        limit:
            limit the number of object it returns. Default is 100.
        order_by:
            specify the order.

    Returns:
        Upon success, a dict of the response. </br>- `data: List`</br>

    <h4>API Endpoint:</h4>
    `/syncs`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Ok. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 422 | Validation Failed. |
    """  # noqa
    client = hightouch_credentials.get_client()
    parsed = await asyncio(client=client)
    return parsed
