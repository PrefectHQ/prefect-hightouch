from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerRunInput")


@attr.s(auto_attribs=True)
class TriggerRunInput:
    """The input of a trigger action to run syncs

    Attributes:
        full_resync (Union[Unset, bool]): Whether to resync all the rows in the query (i.e. ignoring previously
            synced rows). Default: True.
    """

    full_resync: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        full_resync = self.full_resync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_resync is not UNSET:
            field_dict["fullResync"] = full_resync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        full_resync = d.pop("fullResync", UNSET)

        trigger_run_input = cls(
            full_resync=full_resync,
        )

        trigger_run_input.additional_properties = d
        return trigger_run_input

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
