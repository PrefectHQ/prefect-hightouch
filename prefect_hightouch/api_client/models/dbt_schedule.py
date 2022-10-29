from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.dbt_schedule_account import DBTScheduleAccount
from ..models.dbt_schedule_job import DBTScheduleJob

T = TypeVar("T", bound="DBTSchedule")


@attr.s(auto_attribs=True)
class DBTSchedule:
    """
    Attributes:
        account (DBTScheduleAccount):
        dbt_credential_id (str):
        job (DBTScheduleJob):
    """

    account: DBTScheduleAccount
    dbt_credential_id: str
    job: DBTScheduleJob
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account = self.account.to_dict()

        dbt_credential_id = self.dbt_credential_id
        job = self.job.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "dbtCredentialId": dbt_credential_id,
                "job": job,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None:
            return {}
        d = src_dict.copy()
        account = DBTScheduleAccount.from_dict(d.pop("account"))

        dbt_credential_id = d.pop("dbtCredentialId")

        job = DBTScheduleJob.from_dict(d.pop("job"))

        dbt_schedule = cls(
            account=account,
            dbt_credential_id=dbt_credential_id,
            job=job,
        )

        dbt_schedule.additional_properties = d
        return dbt_schedule

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
