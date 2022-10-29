from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SyncRunFailedRows")


@attr.s(auto_attribs=True)
class SyncRunFailedRows:
    """The number of rows that we attempted to sync, but were rejected by the
    destination.

    This does not include rows that weren't attempted due to the sync being
    cancelled.

        Attributes:
            added_count (float): The number of failed adds.
            changed_count (float): The number of failed changes.
            removed_count (float): The number of failed removes.
    """

    added_count: float
    changed_count: float
    removed_count: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        if src_dict is None:
            return {}
        d = src_dict.copy()
        added_count = d.pop("addedCount")

        changed_count = d.pop("changedCount")

        removed_count = d.pop("removedCount")

        sync_run_failed_rows = cls(
            added_count=added_count,
            changed_count=changed_count,
            removed_count=removed_count,
        )

        sync_run_failed_rows.additional_properties = d
        return sync_run_failed_rows

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