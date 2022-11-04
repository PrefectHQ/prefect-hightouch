# This file was auto-generated using prefect-collection-generator,
# However, this file will not be overwritten so freely modify imports
# below, as to override defaults or expose other imports.

from .generated import *  # noqa: F401, F403 isort: skip

HightouchCredentials._logo_url = "https://images.ctfassets.net/gm98wzqotmnx/46tBvip09DRXFuFQBm6mHW/9c03ce91d396006a97d5efe0f718e4cc/hightouch.png?h=250"  # noqa: F405, E501
HightouchCredentials.get_client.__doc__ = """  # F405
Gets a Hightouch REST API Authenticated Client.

Returns:
    A Hightouch REST API Authenticated Client.

Example:
    Gets a Hightouch REST API Authenticated Client.
    ```python
    from prefect import flow
    from prefect_hightouch import HightouchCredentials
    from prefect_hightouch.api_client.api.default import list_sync

    @flow
    def example_get_syncs_flow():
        token = "consumer_key"
        hightouch_credentials = HightouchCredentials(token=token)
        client = hightouch_credentials.get_client()
        syncs = list_sync.sync_detailed(client=client)
        return syncs

    example_get_syncs_flow()
    ```
"""  # noqa: F405
