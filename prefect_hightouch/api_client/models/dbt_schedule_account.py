from typing import Any, Dict, List, Type, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T", bound="DBTScheduleAccount")


class DBTScheduleAccount(BaseModel):
    """
    Attributes:
        id (str):
    """

    id: str = None
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None:
            return {}
        d = src_dict.copy()
        id = d.pop("id")

        dbt_schedule_account = cls(
            id=id,
        )

        dbt_schedule_account.additional_properties = d
        return dbt_schedule_account

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
