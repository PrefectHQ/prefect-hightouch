from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ModelCustom")


@attr.s(auto_attribs=True)
class ModelCustom:
    """Custom query for sources that doesn't support sql. For example, Airtable.

    Attributes:
        query (Any):
    """

    query: Any
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None:
            return {}
        d = src_dict.copy()
        query = d.pop("query")

        model_custom = cls(
            query=query,
        )

        model_custom.additional_properties = d
        return model_custom

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
