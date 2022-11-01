from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordDayBooleanOrUndefined")


class RecordDayBooleanOrUndefined(BaseModel):
    """Construct a type with a set of properties K of type T

    Attributes:
        friday (Union[Unset, bool]):
        monday (Union[Unset, bool]):
        saturday (Union[Unset, bool]):
        sunday (Union[Unset, bool]):
        thursday (Union[Unset, bool]):
        tuesday (Union[Unset, bool]):
        wednesday (Union[Unset, bool]):
    """

    friday: Union[Unset, bool] = UNSET
    monday: Union[Unset, bool] = UNSET
    saturday: Union[Unset, bool] = UNSET
    sunday: Union[Unset, bool] = UNSET
    thursday: Union[Unset, bool] = UNSET
    tuesday: Union[Unset, bool] = UNSET
    wednesday: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        friday = self.friday
        monday = self.monday
        saturday = self.saturday
        sunday = self.sunday
        thursday = self.thursday
        tuesday = self.tuesday
        wednesday = self.wednesday

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if friday is not UNSET:
            field_dict["friday"] = friday
        if monday is not UNSET:
            field_dict["monday"] = monday
        if saturday is not UNSET:
            field_dict["saturday"] = saturday
        if sunday is not UNSET:
            field_dict["sunday"] = sunday
        if thursday is not UNSET:
            field_dict["thursday"] = thursday
        if tuesday is not UNSET:
            field_dict["tuesday"] = tuesday
        if wednesday is not UNSET:
            field_dict["wednesday"] = wednesday

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        friday = d.pop("friday", UNSET)

        monday = d.pop("monday", UNSET)

        saturday = d.pop("saturday", UNSET)

        sunday = d.pop("sunday", UNSET)

        thursday = d.pop("thursday", UNSET)

        tuesday = d.pop("tuesday", UNSET)

        wednesday = d.pop("wednesday", UNSET)

        record_day_boolean_or_undefined = cls(
            friday=friday,
            monday=monday,
            saturday=saturday,
            sunday=sunday,
            thursday=thursday,
            tuesday=tuesday,
            wednesday=wednesday,
        )

        record_day_boolean_or_undefined.additional_properties = d
        return record_day_boolean_or_undefined

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
