# This file was auto-generated using prefect-collection-generator,
# However, this file will not be overwritten so freely modify imports
# below, as to override defaults or expose other imports.

from .generated import *  # noqa: F401, F403 isort: skip

HightouchCredentials._logo_url = "https://images.ctfassets.net/gm98wzqotmnx/6WT9DIXFrqQy0nA9VRZfuL/40a7039742fca9d053677f58a79aacd5/hightouch.png?h=250"  # noqa: F405, E501
HightouchCredentials.get_client.__doc__ = """
Gets a Hightouch REST API Authenticated Client.

Returns:
    A Hightouch REST API Authenticated Client.

Example:
    Gets a Hightouch REST API Authenticated Client and executes the list sync endpoint.
    ```python
    from prefect import flow
    from prefect_hightouch import HightouchCredentials
    from prefect_hightouch.api_client.api.default import list_sync

    @flow
    def example_list_sync_flow():
        token = "consumer_key"
        hightouch_credentials = HightouchCredentials(token=token)
        client = hightouch_credentials.get_client()
        response = list_sync.sync_detailed(client=client)
        syncs = syncs.parsed.data
        return syncs

    example_list_sync_flow()
    ```
"""  # noqa: F405
