import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.sync_run_failed_rows import SyncRunFailedRows
from ..models.sync_run_planned_rows import SyncRunPlannedRows
from ..models.sync_run_status import SyncRunStatus
from ..models.sync_run_successful_rows import SyncRunSuccessfulRows
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncRun")


@attr.s(auto_attribs=True)
class SyncRun:
    """
    Attributes:
        id (str): The sync run's id
        created_at (datetime.datetime): The timestamp when sync run was created. In most cases this will be
            equivalent to `startedAt`, but it may be earlier if the sync was triggered
            while a run was already in progress, and the new run didn't start for
            a while.
        started_at (datetime.datetime): The timestamp when the sync run started
        finished_at (datetime.datetime): The timestamp when the sync run finished
        query_size (float): The number of rows in the query.
        status (SyncRunStatus): The status of sync runs
        completion_ratio (float): The completion ratio of sync run, showing the progress of a sync run
        planned_rows (SyncRunPlannedRows): The number of planned rows that this sync run was supposed to execute.

            Note that the counts for `successfulRows` and `failedRows` may not add up
            to `plannedRows` if the sync was cancelled.
        successful_rows (SyncRunSuccessfulRows): The number of rows that were successfully processed by the destination.
        failed_rows (SyncRunFailedRows): The number of rows that we attempted to sync, but were rejected by the
            destination.

            This does not include rows that weren't attempted due to the sync being
            cancelled.
        error (Union[Unset, str]): Error message if the sync run didn't finish successfully
    """

    id: str
    created_at: datetime.datetime
    started_at: datetime.datetime
    finished_at: datetime.datetime
    query_size: float
    status: SyncRunStatus
    completion_ratio: float
    planned_rows: SyncRunPlannedRows
    successful_rows: SyncRunSuccessfulRows
    failed_rows: SyncRunFailedRows
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_at = self.created_at.isoformat()

        started_at = self.started_at.isoformat()

        finished_at = self.finished_at.isoformat()

        query_size = self.query_size
        status = self.status.value

        completion_ratio = self.completion_ratio
        planned_rows = self.planned_rows.to_dict()

        successful_rows = self.successful_rows.to_dict()

        failed_rows = self.failed_rows.to_dict()

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "startedAt": started_at,
                "finishedAt": finished_at,
                "querySize": query_size,
                "status": status,
                "completionRatio": completion_ratio,
                "plannedRows": planned_rows,
                "successfulRows": successful_rows,
                "failedRows": failed_rows,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created_at = isoparse(d.pop("createdAt"))

        started_at = isoparse(d.pop("startedAt"))

        finished_at = isoparse(d.pop("finishedAt"))

        query_size = d.pop("querySize")

        status = SyncRunStatus(d.pop("status"))

        completion_ratio = d.pop("completionRatio")

        planned_rows = SyncRunPlannedRows.from_dict(d.pop("plannedRows"))

        successful_rows = SyncRunSuccessfulRows.from_dict(d.pop("successfulRows"))

        failed_rows = SyncRunFailedRows.from_dict(d.pop("failedRows"))

        error = d.pop("error", UNSET)

        sync_run = cls(
            id=id,
            created_at=created_at,
            started_at=started_at,
            finished_at=finished_at,
            query_size=query_size,
            status=status,
            completion_ratio=completion_ratio,
            planned_rows=planned_rows,
            successful_rows=successful_rows,
            failed_rows=failed_rows,
            error=error,
        )

        sync_run.additional_properties = d
        return sync_run

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
