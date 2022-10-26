from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.interval import Interval

T = TypeVar("T", bound="IntervalSchedule")


@attr.s(auto_attribs=True)
class IntervalSchedule:
    """
    Attributes:
        interval (Interval):
    """

    interval: Interval
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interval = self.interval.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interval": interval,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interval = Interval.from_dict(d.pop("interval"))

        interval_schedule = cls(
            interval=interval,
        )

        interval_schedule.additional_properties = d
        return interval_schedule

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
