from typing import Any, Dict, List, Type, TypeVar

from pydantic import VERSION as PYDANTIC_VERSION

if PYDANTIC_VERSION.startswith("2."):
    from pydantic.v1 import BaseModel, Field
else:
    from pydantic import BaseModel, Field

from ..models.dbt_schedule_account import DBTScheduleAccount
from ..models.dbt_schedule_job import DBTScheduleJob
from ..types import UNSET

T = TypeVar("T", bound="DBTSchedule")


class DBTSchedule(BaseModel):
    """
    Attributes:
        account (DBTScheduleAccount):
        dbt_credential_id (str):
        job (DBTScheduleJob):
    """

    account: DBTScheduleAccount = None
    dbt_credential_id: str = None
    job: DBTScheduleJob = None
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

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
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
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
