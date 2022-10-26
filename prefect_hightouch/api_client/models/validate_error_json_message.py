from enum import Enum


class ValidateErrorJSONMessage(str, Enum):
    VALIDATION_FAILED = "Validation failed"

    def __str__(self) -> str:
        return str(self.value)
