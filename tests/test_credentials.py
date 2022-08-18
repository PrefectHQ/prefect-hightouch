import pytest
from httpx import AsyncClient

from prefect_hightouch import HightouchCredentials


@pytest.mark.parametrize("token", [None, "token_value"])
def test_hightouch_credentials_get_client(token):
    client = HightouchCredentials(token=token).get_client()
    assert isinstance(client, AsyncClient)
    if token is not None:
        assert client.headers["authorization"] == "Bearer token_value"
