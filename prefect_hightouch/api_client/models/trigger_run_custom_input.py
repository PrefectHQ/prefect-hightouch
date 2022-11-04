from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerRunCustomInput")


class TriggerRunCustomInput(BaseModel):
    """The input of a trigger action to run syncs based on sync ID, slug or other filters

    Attributes:
        full_resync (Union[Unset, bool]): Whether to resync all the rows in the query (i.e. ignoring previously
            synced rows). Default: True.
        sync_id (Union[Unset, str]): Trigger run based on sync id
        sync_slug (Union[Unset, str]): Trigger run based on sync slug
    """

    full_resync: Union[Unset, bool] = True
    sync_id: Union[Unset, str] = UNSET
    sync_slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        full_resync = self.full_resync
        sync_id = self.sync_id
        sync_slug = self.sync_slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_resync is not UNSET:
            field_dict["fullResync"] = full_resync
        if sync_id is not UNSET:
            field_dict["syncId"] = sync_id
        if sync_slug is not UNSET:
            field_dict["syncSlug"] = sync_slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        full_resync = d.pop("fullResync", UNSET)

        sync_id = d.pop("syncId", UNSET)

        sync_slug = d.pop("syncSlug", UNSET)

        trigger_run_custom_input = cls(
            full_resync=full_resync,
            sync_id=sync_id,
            sync_slug=sync_slug,
        )

        trigger_run_custom_input.additional_properties = d
        return trigger_run_custom_input

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
