from enum import Enum


class ListSyncRunsOrderBy(str, Enum):
    ID = "id"
    CREATEDAT = "createdAt"
    STARTEDAT = "startedAt"
    FINISHEDAT = "finishedAt"

    def __str__(self) -> str:
        return str(self.value)
