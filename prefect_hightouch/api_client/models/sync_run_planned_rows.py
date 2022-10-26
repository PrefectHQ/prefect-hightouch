from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SyncRunPlannedRows")


@attr.s(auto_attribs=True)
class SyncRunPlannedRows:
    """The number of planned rows that this sync run was supposed to execute.

    Note that the counts for `successfulRows` and `failedRows` may not add up
    to `plannedRows` if the sync was cancelled.

        Attributes:
            removed_count (float): The number of removed rows.
            changed_count (float): The number of changed rows.
            added_count (float): The number of added rows.
    """

    removed_count: float
    changed_count: float
    added_count: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        removed_count = self.removed_count
        changed_count = self.changed_count
        added_count = self.added_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "removedCount": removed_count,
                "changedCount": changed_count,
                "addedCount": added_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        removed_count = d.pop("removedCount")

        changed_count = d.pop("changedCount")

        added_count = d.pop("addedCount")

        sync_run_planned_rows = cls(
            removed_count=removed_count,
            changed_count=changed_count,
            added_count=added_count,
        )

        sync_run_planned_rows.additional_properties = d
        return sync_run_planned_rows

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
