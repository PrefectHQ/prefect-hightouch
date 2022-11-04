"""
This is a module containing exceptions used within prefect-hightouch.
"""

from prefect_hightouch.api_client.models import SyncStatus


class HightouchSyncRunError(RuntimeError):
    """
    A generic Hightouch sync exception.
    """


class HightouchSyncRunTimedOut(HightouchSyncRunError):
    """
    Raised when Hightouch sync run does not complete in the configured max
    wait seconds.
    """


class HightouchSyncRunDisabled(HightouchSyncRunError):
    """
    Raised when Hightouch sync run is disabled.
    """


class HightouchSyncRunCancelled(HightouchSyncRunError):
    """
    Raised when Hightouch sync run is cancelled.
    """


class HightouchSyncRunFailed(HightouchSyncRunError):
    """
    Raised when Hightouch sync run is failed.
    """


class HightouchSyncRunInterrupted(HightouchSyncRunError):
    """
    Raised when Hightouch sync run is interrupted.
    """


TERMINAL_STATUS_EXCEPTIONS = {
    SyncStatus.DISABLED: HightouchSyncRunDisabled,
    SyncStatus.CANCELLED: HightouchSyncRunCancelled,
    SyncStatus.FAILED: HightouchSyncRunFailed,
    SyncStatus.INTERRUPTED: HightouchSyncRunInterrupted,
    SyncStatus.SUCCESS: None,
}
