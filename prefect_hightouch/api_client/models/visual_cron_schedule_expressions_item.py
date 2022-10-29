from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.record_day_boolean_or_undefined import RecordDayBooleanOrUndefined

T = TypeVar("T", bound="VisualCronScheduleExpressionsItem")


@attr.s(auto_attribs=True)
class VisualCronScheduleExpressionsItem:
    """
    Attributes:
        days (RecordDayBooleanOrUndefined): Construct a type with a set of properties K of type T
        time (str):
    """

    days: RecordDayBooleanOrUndefined
    time: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days = self.days.to_dict()

        time = self.time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days": days,
                "time": time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None:
            return {}
        d = src_dict.copy()
        days = RecordDayBooleanOrUndefined.from_dict(d.pop("days"))

        time = d.pop("time")

        visual_cron_schedule_expressions_item = cls(
            days=days,
            time=time,
        )

        visual_cron_schedule_expressions_item.additional_properties = d
        return visual_cron_schedule_expressions_item

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
