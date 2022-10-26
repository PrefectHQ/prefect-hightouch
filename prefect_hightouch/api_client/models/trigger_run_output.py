from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TriggerRunOutput")


@attr.s(auto_attribs=True)
class TriggerRunOutput:
    """The output of a trigger action to run syncs

    Attributes:
        id (str): The id of the triggered sync run. This can be passed to `/sync/runs` to
            get the run's status.
    """

    id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        trigger_run_output = cls(
            id=id,
        )

        trigger_run_output.additional_properties = d
        return trigger_run_output

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
