from enum import Enum


class ListDestinationOrderBy(str, Enum):
    ID = "id"
    NAME = "name"
    SLUG = "slug"
    CREATEDAT = "createdAt"
    UPDATEDAT = "updatedAt"

    def __str__(self) -> str:
        return str(self.value)
