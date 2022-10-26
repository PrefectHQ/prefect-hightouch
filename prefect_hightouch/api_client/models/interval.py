from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.interval_unit import IntervalUnit

T = TypeVar("T", bound="Interval")


@attr.s(auto_attribs=True)
class Interval:
    """
    Attributes:
        unit (IntervalUnit):
        quantity (float):
    """

    unit: IntervalUnit
    quantity: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit = self.unit.value

        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unit": unit,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit = IntervalUnit(d.pop("unit"))

        quantity = d.pop("quantity")

        interval = cls(
            unit=unit,
            quantity=quantity,
        )

        interval.additional_properties = d
        return interval

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
