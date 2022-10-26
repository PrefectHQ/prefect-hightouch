from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ModelVisual")


@attr.s(auto_attribs=True)
class ModelVisual:
    """Visual query, used by audience

    Attributes:
        secondary_label (str):
        primary_label (str):
        filter_ (Any):
        parent_id (str): Parent id of the schema that visual query is based on
    """

    secondary_label: str
    primary_label: str
    filter_: Any
    parent_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        secondary_label = self.secondary_label
        primary_label = self.primary_label
        filter_ = self.filter_
        parent_id = self.parent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secondaryLabel": secondary_label,
                "primaryLabel": primary_label,
                "filter": filter_,
                "parentId": parent_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        secondary_label = d.pop("secondaryLabel")

        primary_label = d.pop("primaryLabel")

        filter_ = d.pop("filter")

        parent_id = d.pop("parentId")

        model_visual = cls(
            secondary_label=secondary_label,
            primary_label=primary_label,
            filter_=filter_,
            parent_id=parent_id,
        )

        model_visual.additional_properties = d
        return model_visual

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
