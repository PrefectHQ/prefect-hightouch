# prefect-hightouch

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-hightouch/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-hightouch?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/PrefectHQ/prefect-hightouch/" alt="Stars">
        <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-hightouch?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-hightouch/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-hightouch?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/PrefectHQ/prefect-hightouch/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-hightouch?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>

## Welcome!

Prefect integrations for interacting with Hightouch.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-hightouch` with `pip`:

```bash
pip install prefect-hightouch
```

Then, register to [view the block](https://orion-docs.prefect.io/ui/blocks/) on Prefect Cloud:

```bash
prefect block register -m prefect_hightouch.credentials
```

Note, to use the `load` method on Blocks, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).

### List, get, and trigger syncs

```python
from prefect import flow
from prefect_hightouch import HightouchCredentials, api_models
from prefect_hightouch.syncs import (
    list_sync,
    get_sync,
    list_sync_runs,
    trigger_run,
    trigger_run_custom,
)

@flow
def hightouch_sync_flow():
    hightouch_credentials = HightouchCredentials.load("hightouch-token")

    # list all syncs
    syncs = list_sync(
        hightouch_credentials, order_by=api_models.ListSyncOrderBy.CREATEDAT
    )

    # get first sync
    sync_id = syncs[0].id
    sync = get_sync(hightouch_credentials, sync_id)

    # list previous runs
    sync_runs = list_sync_runs(hightouch_credentials, sync_id)

    # trigger by id
    sync_run = trigger_run(
        hightouch_credentials,
        sync_id,
        json_body=api_models.TriggerRunInput(full_resync=False),
    )

    # trigger by slug
    sync_slug = syncs[0].slug
    sync_run_2 = trigger_run_custom(
        hightouch_credentials,
        json_body=api_models.TriggerRunCustomInput(
            sync_slug=sync_slug,
            full_resync=False,
        ),
    )
    return sync_runs

hightouch_sync_flow()
```

## Resources

If you encounter any bugs while using `prefect-hightouch`, feel free to open an issue in the [prefect-hightouch](https://github.com/PrefectHQ/prefect-hightouch) repository.

If you have any questions or issues while using `prefect-hightouch`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to ⭐️ or watch [`prefect-hightouch`](https://github.com/PrefectHQ/prefect-hightouch) for updates too!

## Development

If you'd like to install a version of `prefect-hightouch` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-hightouch.git

cd prefect-hightouch/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
