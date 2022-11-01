""" Contains methods for accessing the API """

import functools
from typing import Callable, TypeVar

from typing_extensions import Concatenate, ParamSpec

from ...credentials import HightouchCredentials
from ..client import AuthenticatedClient

C = ParamSpec("C")  # client function
T = ParamSpec("T")  # task function
R = TypeVar("R")  # The return type of the API function


def _execute_endpoint(
    endpoint_fn: Callable[Concatenate[AuthenticatedClient, C], R]
) -> Callable[[Callable[C, R]], Callable[Concatenate[HightouchCredentials, C], R]]:
    def wrap(task_fn: Callable[T, R]) -> Callable[T, R]:
        @functools.wraps(task_fn)
        async def run(*args: T.args, **kwargs: T.kwargs) -> R:
            hightouch_credentials = None
            if "hightouch_credentials" in kwargs:
                hightouch_credentials = kwargs.pop("hightouch_credentials")
                input_args = args
            else:
                hightouch_credentials = args[0]
                input_args = args[1:]
            kwargs["client"] = hightouch_credentials.get_client()
            parsed_response = await endpoint_fn(*input_args, **kwargs)
            if hasattr(parsed_response, "data"):
                parsed_response = parsed_response.data
            return parsed_response

        return run

    return wrap
