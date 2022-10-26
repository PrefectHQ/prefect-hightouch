from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerRunCustomInput")


@attr.s(auto_attribs=True)
class TriggerRunCustomInput:
    """The input of a trigger action to run syncs based on sync ID, slug or other filters

    Attributes:
        sync_slug (Union[Unset, str]): Trigger run based on sync slug
        sync_id (Union[Unset, str]): Trigger run based on sync id
        full_resync (Union[Unset, bool]): Whether to resync all the rows in the query (i.e. ignoring previously
            synced rows). Default: True.
    """

    sync_slug: Union[Unset, str] = UNSET
    sync_id: Union[Unset, str] = UNSET
    full_resync: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sync_slug = self.sync_slug
        sync_id = self.sync_id
        full_resync = self.full_resync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sync_slug is not UNSET:
            field_dict["syncSlug"] = sync_slug
        if sync_id is not UNSET:
            field_dict["syncId"] = sync_id
        if full_resync is not UNSET:
            field_dict["fullResync"] = full_resync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sync_slug = d.pop("syncSlug", UNSET)

        sync_id = d.pop("syncId", UNSET)

        full_resync = d.pop("fullResync", UNSET)

        trigger_run_custom_input = cls(
            sync_slug=sync_slug,
            sync_id=sync_id,
            full_resync=full_resync,
        )

        trigger_run_custom_input.additional_properties = d
        return trigger_run_custom_input

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
