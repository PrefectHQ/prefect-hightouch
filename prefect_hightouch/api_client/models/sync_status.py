from enum import Enum


class SyncStatus(str, Enum):
    DISABLED = "disabled"
    PENDING = "pending"
    CANCELLED = "cancelled"
    FAILED = "failed"
    QUEUED = "queued"
    SUCCESS = "success"
    WARNING = "warning"
    QUERYING = "querying"
    PROCESSING = "processing"
    REPORTING = "reporting"
    INTERRUPTED = "interrupted"

    def __str__(self) -> str:
        return str(self.value)
