from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.cron_schedule import CronSchedule
from ..models.dbt_schedule import DBTSchedule
from ..models.interval_schedule import IntervalSchedule
from ..models.visual_cron_schedule import VisualCronSchedule
from ..types import UNSET

T = TypeVar("T", bound="SyncSchedule")


class SyncSchedule(BaseModel):
    """The scheduling configuration. It can be triggerd based on several ways:

    Interval: the sync will be trigged based on certain interval(minutes/hours/days/weeks)

    Cron: the sync will be trigged based on cron expression https://en.wikipedia.org/wiki/Cron.

    Visual: the sync will be trigged based a visual cron configuration on UI

    DBT-cloud: the sync will be trigged based on a dbt cloud job

        Attributes:
            schedule (Union[CronSchedule, DBTSchedule, IntervalSchedule, VisualCronSchedule]):
            type (str):
    """

    schedule: Union[
        CronSchedule, DBTSchedule, IntervalSchedule, VisualCronSchedule
    ] = None
    type: str = None
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schedule: Dict[str, Any]

        if isinstance(self.schedule, IntervalSchedule):
            schedule = self.schedule.to_dict()

        elif isinstance(self.schedule, CronSchedule):
            schedule = self.schedule.to_dict()

        elif isinstance(self.schedule, VisualCronSchedule):
            schedule = self.schedule.to_dict()

        else:
            schedule = self.schedule.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule": schedule,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}

        def _parse_schedule(
            data: object,
        ) -> Union[CronSchedule, DBTSchedule, IntervalSchedule, VisualCronSchedule]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_type_0 = IntervalSchedule.from_dict(data)

                return schedule_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_type_1 = CronSchedule.from_dict(data)

                return schedule_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_type_2 = VisualCronSchedule.from_dict(data)

                return schedule_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            schedule_type_3 = DBTSchedule.from_dict(data)

            return schedule_type_3

        schedule = _parse_schedule(d.pop("schedule"))

        type = d.pop("type")

        sync_schedule = cls(
            schedule=schedule,
            type=type,
        )

        sync_schedule.additional_properties = d
        return sync_schedule

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
