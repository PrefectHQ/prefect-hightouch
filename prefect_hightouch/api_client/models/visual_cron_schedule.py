from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.visual_cron_schedule_expressions_item import (
    VisualCronScheduleExpressionsItem,
)

T = TypeVar("T", bound="VisualCronSchedule")


@attr.s(auto_attribs=True)
class VisualCronSchedule:
    """
    Attributes:
        expressions (List[VisualCronScheduleExpressionsItem]):
    """

    expressions: List[VisualCronScheduleExpressionsItem]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expressions = []
        for expressions_item_data in self.expressions:
            expressions_item = expressions_item_data.to_dict()

            expressions.append(expressions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expressions": expressions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None:
            return {}
        d = src_dict.copy()
        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = VisualCronScheduleExpressionsItem.from_dict(
                expressions_item_data
            )

            expressions.append(expressions_item)

        visual_cron_schedule = cls(
            expressions=expressions,
        )

        visual_cron_schedule.additional_properties = d
        return visual_cron_schedule

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