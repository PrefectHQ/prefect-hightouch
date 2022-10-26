from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SourceConfiguration")


@attr.s(auto_attribs=True)
class SourceConfiguration:
    """The source's configuration. This specifies general metadata about sources, like connection details
    Hightouch will use this configuration to connect to underlying source.

    The schema depends on the destination.

    Consumers should NOT make assumptions on the contents of the
    configuration. It may change as Hightouch updates its internal code.

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_configuration = cls()

        source_configuration.additional_properties = d
        return source_configuration

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
