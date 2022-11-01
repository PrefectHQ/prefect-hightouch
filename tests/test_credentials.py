from prefect_hightouch import HightouchCredentials
from prefect_hightouch.api_client.client import AuthenticatedClient


def test_hightouch_credentials_get_client():
    client = HightouchCredentials(token="token_value").get_client()
    assert isinstance(client, AuthenticatedClient)
    assert client.auth_header_name == "Authorization"
    assert client.token == "token_value"
