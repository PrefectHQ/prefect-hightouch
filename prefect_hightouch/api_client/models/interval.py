from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.interval_unit import IntervalUnit

T = TypeVar("T", bound="Interval")


@attr.s(auto_attribs=True)
class Interval:
    """
    Attributes:
        quantity (float):
        unit (IntervalUnit):
    """

    quantity: float
    unit: IntervalUnit
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity
        unit = self.unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None:
            return {}
        d = src_dict.copy()
        quantity = d.pop("quantity")

        unit = IntervalUnit(d.pop("unit"))

        interval = cls(
            quantity=quantity,
            unit=unit,
        )

        interval.additional_properties = d
        return interval

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
