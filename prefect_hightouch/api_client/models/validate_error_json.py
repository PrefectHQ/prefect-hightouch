from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.validate_error_json_details import ValidateErrorJSONDetails
from ..models.validate_error_json_message import ValidateErrorJSONMessage

T = TypeVar("T", bound="ValidateErrorJSON")


@attr.s(auto_attribs=True)
class ValidateErrorJSON:
    """
    Attributes:
        message (ValidateErrorJSONMessage):
        details (ValidateErrorJSONDetails):
    """

    message: ValidateErrorJSONMessage
    details: ValidateErrorJSONDetails
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message.value

        details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "details": details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = ValidateErrorJSONMessage(d.pop("message"))

        details = ValidateErrorJSONDetails.from_dict(d.pop("details"))

        validate_error_json = cls(
            message=message,
            details=details,
        )

        validate_error_json.additional_properties = d
        return validate_error_json

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
