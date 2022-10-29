from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ModelVisual")


@attr.s(auto_attribs=True)
class ModelVisual:
    """Visual query, used by audience

    Attributes:
        filter_ (Any):
        parent_id (str): Parent id of the schema that visual query is based on
        primary_label (str):
        secondary_label (str):
    """

    filter_: Any
    parent_id: str
    primary_label: str
    secondary_label: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_ = self.filter_
        parent_id = self.parent_id
        primary_label = self.primary_label
        secondary_label = self.secondary_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter": filter_,
                "parentId": parent_id,
                "primaryLabel": primary_label,
                "secondaryLabel": secondary_label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filter_ = d.pop("filter")

        parent_id = d.pop("parentId")

        primary_label = d.pop("primaryLabel")

        secondary_label = d.pop("secondaryLabel")

        model_visual = cls(
            filter_=filter_,
            parent_id=parent_id,
            primary_label=primary_label,
            secondary_label=secondary_label,
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
