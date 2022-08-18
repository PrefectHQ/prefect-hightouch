"""Credential classes used to perform authenticated interactions with Hightouch"""

from typing import Optional

from httpx import AsyncClient
from prefect.blocks.core import Block
from pydantic import SecretStr


class HightouchCredentials(Block):
    """
    Block used to manage Hightouch authentication.

    Args:
        token: the token to authenticate with Hightouch.

    Examples:
        Load stored Hightouch credentials:
        ```python
        from prefect_hightouch import HightouchCredentials
        hightouch_credentials_block = HightouchCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "Hightouch Credentials"
    # _logo_url = "<LOGO_URL_HERE>"  # noqa

    token: Optional[SecretStr] = None

    def get_client(self) -> AsyncClient:
        """
        Gets an authenticated Hightouch REST AsyncClient.

        Returns:
            An authenticated Hightouch REST AsyncClient

        Example:
            Gets an authenticated Hightouch REST AsyncClient.
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
        base_url = f"https://api.hightouch.com/api/v1"

        if self.token is not None:
            headers = {"Authorization": f"Bearer {self.token.get_secret_value()}"}
        else:
            headers = None

        client = AsyncClient(base_url=base_url, headers=headers)
        return client
