import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from dateutil.parser import isoparse
from pydantic import BaseModel, Field

from ..models.sync_run_failed_rows import SyncRunFailedRows
from ..models.sync_run_planned_rows import SyncRunPlannedRows
from ..models.sync_run_status import SyncRunStatus
from ..models.sync_run_successful_rows import SyncRunSuccessfulRows
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncRun")


class SyncRun(BaseModel):
    """
    Attributes:
        completion_ratio (float): The completion ratio of sync run, showing the progress of a sync run
        created_at (datetime.datetime): The timestamp when sync run was created. In most cases this will be
            equivalent to `startedAt`, but it may be earlier if the sync was triggered
            while a run was already in progress, and the new run didn't start for
            a while.
        failed_rows (SyncRunFailedRows): The number of rows that we attempted to sync, but were rejected by the
            destination.

            This does not include rows that weren't attempted due to the sync being
            cancelled.
        finished_at (datetime.datetime): The timestamp when the sync run finished
        id (str): The sync run's id
        planned_rows (SyncRunPlannedRows): The number of planned rows that this sync run was supposed to execute.

            Note that the counts for `successfulRows` and `failedRows` may not add up
            to `plannedRows` if the sync was cancelled.
        query_size (float): The number of rows in the query.
        started_at (datetime.datetime): The timestamp when the sync run started
        status (SyncRunStatus): The status of sync runs
        successful_rows (SyncRunSuccessfulRows): The number of rows that were successfully processed by the destination.
        error (Union[Unset, str]): Error message if the sync run didn't finish successfully
    """

    completion_ratio: float = None
    created_at: datetime.datetime = None
    failed_rows: SyncRunFailedRows = None
    finished_at: datetime.datetime = None
    id: str = None
    planned_rows: SyncRunPlannedRows = None
    query_size: float = None
    started_at: datetime.datetime = None
    status: SyncRunStatus = None
    successful_rows: SyncRunSuccessfulRows = None
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completion_ratio = self.completion_ratio
        created_at = self.created_at.isoformat()

        failed_rows = self.failed_rows.to_dict()

        finished_at = self.finished_at.isoformat()

        id = self.id
        planned_rows = self.planned_rows.to_dict()

        query_size = self.query_size
        started_at = self.started_at.isoformat()

        status = self.status.value

        successful_rows = self.successful_rows.to_dict()

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completionRatio": completion_ratio,
                "createdAt": created_at,
                "failedRows": failed_rows,
                "finishedAt": finished_at,
                "id": id,
                "plannedRows": planned_rows,
                "querySize": query_size,
                "startedAt": started_at,
                "status": status,
                "successfulRows": successful_rows,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        completion_ratio = d.pop("completionRatio")

        created_at = isoparse(d.pop("createdAt"))

        failed_rows = SyncRunFailedRows.from_dict(d.pop("failedRows"))

        finished_at = isoparse(d.pop("finishedAt"))

        id = d.pop("id")

        planned_rows = SyncRunPlannedRows.from_dict(d.pop("plannedRows"))

        query_size = d.pop("querySize")

        started_at = isoparse(d.pop("startedAt"))

        status = SyncRunStatus(d.pop("status"))

        successful_rows = SyncRunSuccessfulRows.from_dict(d.pop("successfulRows"))

        error = d.pop("error", UNSET)

        sync_run = cls(
            completion_ratio=completion_ratio,
            created_at=created_at,
            failed_rows=failed_rows,
            finished_at=finished_at,
            id=id,
            planned_rows=planned_rows,
            query_size=query_size,
            started_at=started_at,
            status=status,
            successful_rows=successful_rows,
            error=error,
        )

        sync_run.additional_properties = d
        return sync_run

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
