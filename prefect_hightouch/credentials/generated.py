"""
This is a module containing credentials, auto-generated, used
to perform authenticated interactions with Hightouch.
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module is outdated
# rerun scripts/generate.py. To override the default generated output:
# 1. create a separate module and rewrite the class / function
# 2. import in `__init__.py`, under the `from .generated import *` line
# 3. hide the generated function in `docs/.md` under `options`


from typing import Any, Dict

from prefect.blocks.core import Block
from pydantic import Field, SecretStr

from prefect_hightouch.api_client.client import AuthenticatedClient


class HightouchCredentials(Block):
    """
    Block used to manage Hightouch authentication.

    Attributes:
        token: The token to authenticate with Hightouch.

        timeout: Number of seconds before the request times out.
        client_kwargs: Additional keyword arguments to pass to
            `prefect_hightouch.api_client.client.AuthenticatedClient`.

    Examples:
        Load stored Hightouch credentials:
        ```python
        from prefect_hightouch import HightouchCredentials
        hightouch_credentials_block = HightouchCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "Hightouch Credentials"
    # _logo_url = "<UPDATE _logo_url IN __init__.py>"  # noqa

    token: SecretStr = Field(default=..., description="Token used for authentication.")
    timeout: float = Field(
        default=5.0, description="Number of seconds before the request times out."
    )
    client_kwargs: Dict[str, Any] = Field(
        default_factory=dict,
        title="Additional configuration",
        description=(
            "Additional keyword arguments to pass to "
            "`prefect_hightouch.api_client.client.AuthenticatedClient`."
        ),
    )

    def get_client(self) -> AuthenticatedClient:
        """
        Gets a Hightouch REST API Authenticated Client.

        Returns:
            A Hightouch REST API Authenticated Client.

        Example:
            Gets a Hightouch REST API Authenticated Client.
            ```python
            from prefect import flow
            from prefect_hightouch import HightouchCredentials

            @flow
            def example_get_client_flow():
                token = "consumer_key"
                hightouch_credentials = HightouchCredentials(token=token)
                client = hightouch_credentials.get_client()
                return client

            example_get_client_flow()
            ```
        """

        base_url = "https://api.hightouch.com/api/v1"

        client_kwargs = self.client_kwargs.copy()
        token = self.token.get_secret_value()
        prefix = "Bearer"
        client = AuthenticatedClient(
            base_url=base_url,
            token=token,
            prefix=prefix,
            timeout=self.timeout,
            **client_kwargs
        )
        return client
