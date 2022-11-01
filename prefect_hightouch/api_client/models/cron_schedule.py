from typing import Any, Dict, List, Type, TypeVar

from pydantic import BaseModel, Field

from ..types import UNSET

T = TypeVar("T", bound="CronSchedule")


class CronSchedule(BaseModel):
    """
    Attributes:
        expression (str):
    """

    expression: str = None
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expression = self.expression

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expression": expression,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        expression = d.pop("expression")

        cron_schedule = cls(
            expression=expression,
        )

        cron_schedule.additional_properties = d
        return cron_schedule

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
