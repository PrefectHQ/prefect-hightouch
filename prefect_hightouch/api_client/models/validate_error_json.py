from typing import Any, Dict, List, Type, TypeVar

from pydantic import BaseModel, Field

from ..models.validate_error_json_details import ValidateErrorJSONDetails
from ..models.validate_error_json_message import ValidateErrorJSONMessage
from ..types import UNSET

T = TypeVar("T", bound="ValidateErrorJSON")


class ValidateErrorJSON(BaseModel):
    """
    Attributes:
        details (ValidateErrorJSONDetails):
        message (ValidateErrorJSONMessage):
    """

    details: ValidateErrorJSONDetails = None
    message: ValidateErrorJSONMessage = None
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        details = self.details.to_dict()

        message = self.message.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "details": details,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        details = ValidateErrorJSONDetails.from_dict(d.pop("details"))

        message = ValidateErrorJSONMessage(d.pop("message"))

        validate_error_json = cls(
            details=details,
            message=message,
        )

        validate_error_json.additional_properties = d
        return validate_error_json

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
