""" Contains some shared types for properties """
from http import HTTPStatus
from typing import BinaryIO, Generic, MutableMapping, Optional, Tuple, TypeVar

from pydantic import VERSION as PYDANTIC_VERSION

if PYDANTIC_VERSION.startswith("2."):
    from pydantic.v1 import BaseModel
    from pydantic.v1.generics import GenericModel
else:
    from pydantic import BaseModel
    from pydantic.generics import GenericModel


class Unset(BaseModel):
    def __bool__(self) -> bool:
        return False


UNSET: Unset = Unset()

FileJsonType = Tuple[Optional[str], BinaryIO, Optional[str]]


class File:
    """Contains information for file uploads"""

    payload: BinaryIO
    file_name: Optional[str] = None
    mime_type: Optional[str] = None

    def to_tuple(self) -> FileJsonType:
        """Return a tuple representation that httpx will accept for multipart/form-data"""
        return self.file_name, self.payload, self.mime_type


T = TypeVar("T")


class Response(GenericModel, Generic[T]):
    """A response from an endpoint"""

    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: Optional[T]


__all__ = ["File", "Response", "FileJsonType"]
