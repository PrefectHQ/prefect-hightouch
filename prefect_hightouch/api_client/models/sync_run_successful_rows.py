from typing import Any, Dict, List, Type, TypeVar

from pydantic import BaseModel, Field

from ..types import UNSET

T = TypeVar("T", bound="SyncRunSuccessfulRows")


class SyncRunSuccessfulRows(BaseModel):
    """The number of rows that were successfully processed by the destination.

    Attributes:
        added_count (float): The number of successful adds.
        changed_count (float): The number of successful changes.
        removed_count (float): The number of successful removes.
    """

    added_count: float = None
    changed_count: float = None
    removed_count: float = None
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        added_count = self.added_count
        changed_count = self.changed_count
        removed_count = self.removed_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addedCount": added_count,
                "changedCount": changed_count,
                "removedCount": removed_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        added_count = d.pop("addedCount")

        changed_count = d.pop("changedCount")

        removed_count = d.pop("removedCount")

        sync_run_successful_rows = cls(
            added_count=added_count,
            changed_count=changed_count,
            removed_count=removed_count,
        )

        sync_run_successful_rows.additional_properties = d
        return sync_run_successful_rows

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
