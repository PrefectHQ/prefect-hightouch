# prefect-hightouch

<a href="https://pypi.python.org/pypi/prefect-hightouch/" alt="PyPI Version">
    <img src="https://badge.fury.io/py/prefect-hightouch.svg" /></a>
<a href="https://github.com/PrefectHQ/prefect-hightouch/" alt="Stars">
    <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-hightouch" /></a>
<a href="https://pepy.tech/badge/prefect-hightouch/" alt="Downloads">
    <img src="https://pepy.tech/badge/prefect-hightouch" /></a>
<a href="https://github.com/PrefectHQ/prefect-hightouch/pulse" alt="Activity">
    <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-hightouch" /></a>
<a href="https://github.com/PrefectHQ/prefect-hightouch/graphs/contributors" alt="Contributors">
    <img src="https://img.shields.io/github/contributors/PrefectHQ/prefect-hightouch" /></a>
<br>
<a href="https://prefect-community.slack.com" alt="Slack">
    <img src="https://img.shields.io/badge/slack-join_community-red.svg?logo=slack" /></a>
<a href="https://discourse.prefect.io/" alt="Discourse">
    <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?logo=discourse" /></a>

## Welcome!

Prefect integrations for interacting with Hightouch.

The tasks within this collection were created by a code generator using the service's OpenAPI spec.

The service's REST API documentation can be found [here](replace_this_with_link_to_api_docs).

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

### Write and run a flow

```python
from prefect import flow
from prefect_hightouch.tasks import (
    goodbye_prefect_hightouch,
    hello_prefect_hightouch,
)


@flow
def example_flow():
    hello_prefect_hightouch
    goodbye_prefect_hightouch

example_flow()
```

## Resources

If you encounter any bugs while using `prefect-hightouch`, feel free to open an issue in the [prefect-hightouch](https://github.com/PrefectHQ/prefect-hightouch) repository.

If you have any questions or issues while using `prefect-hightouch`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-hightouch` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-hightouch.git

cd prefect-hightouch/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
