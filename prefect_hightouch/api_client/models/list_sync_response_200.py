from typing import Any, Dict, List, Type, TypeVar

from pydantic import BaseModel, Field

from ..models.sync import Sync
from ..types import UNSET

T = TypeVar("T", bound="ListSyncResponse200")


class ListSyncResponse200(BaseModel):
    """
    Attributes:
        data (List[Sync]):
    """

    data: List[Sync] = None
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Sync.from_dict(data_item_data)

            data.append(data_item)

        list_sync_response_200 = cls(
            data=data,
        )

        list_sync_response_200.additional_properties = d
        return list_sync_response_200

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
