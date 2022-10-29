import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..models.sync_configuration import SyncConfiguration
from ..models.sync_schedule import SyncSchedule
from ..models.sync_status import SyncStatus

T = TypeVar("T", bound="Sync")


@attr.s(auto_attribs=True)
class Sync:
    """Syncs define how data from models are mapped to destinations. Each time a
    sync runs, Hightouch calculates the rows that have changed since the last
    run, and syncs them to Sync's destination.

        Attributes:
            configuration (SyncConfiguration): The sync's configuration. This specifies how data is mapped, among other
                configuration.

                The schema depends on the destination.

                Consumers should NOT make assumptions on the contents of the
                configuration. It may change as Hightouch updates its internal code.
            created_at (datetime.datetime): The timestamp when the sync was created
            destination_id (str): The id of the Destination that sync is connected to
            disabled (bool): Whether the sync has been disabled by the user.
            id (str): The sync's id
            last_run_at (datetime.datetime): The timestamp of the last sync run
            model_id (str): The id of the Model that sync is connected to
            primary_key (str): The primary key that sync uses to identify data from source
            referenced_columns (List[str]): The reference column that sync depends on to sync data from source
            schedule (SyncSchedule): The scheduling configuration. It can be triggerd based on several ways:

                Interval: the sync will be trigged based on certain interval(minutes/hours/days/weeks)

                Cron: the sync will be trigged based on cron expression https://en.wikipedia.org/wiki/Cron.

                Visual: the sync will be trigged based a visual cron configuration on UI

                DBT-cloud: the sync will be trigged based on a dbt cloud job
            slug (str): The sync's slug
            status (SyncStatus):
            updated_at (datetime.datetime): The timestamp when the sync was last updated
            workspace_id (str): The id of the workspace that the sync belongs to
    """

    configuration: SyncConfiguration
    created_at: datetime.datetime
    destination_id: str
    disabled: bool
    id: str
    last_run_at: datetime.datetime
    model_id: str
    primary_key: str
    referenced_columns: List[str]
    schedule: SyncSchedule
    slug: str
    status: SyncStatus
    updated_at: datetime.datetime
    workspace_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        configuration = self.configuration.to_dict()

        created_at = self.created_at.isoformat()

        destination_id = self.destination_id
        disabled = self.disabled
        id = self.id
        last_run_at = self.last_run_at.isoformat()

        model_id = self.model_id
        primary_key = self.primary_key
        referenced_columns = self.referenced_columns

        schedule = self.schedule.to_dict()

        slug = self.slug
        status = self.status.value

        updated_at = self.updated_at.isoformat()

        workspace_id = self.workspace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "createdAt": created_at,
                "destinationId": destination_id,
                "disabled": disabled,
                "id": id,
                "lastRunAt": last_run_at,
                "modelId": model_id,
                "primaryKey": primary_key,
                "referencedColumns": referenced_columns,
                "schedule": schedule,
                "slug": slug,
                "status": status,
                "updatedAt": updated_at,
                "workspaceId": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None:
            return {}
        d = src_dict.copy()
        configuration = SyncConfiguration.from_dict(d.pop("configuration"))

        created_at = isoparse(d.pop("createdAt"))

        destination_id = d.pop("destinationId")

        disabled = d.pop("disabled")

        id = d.pop("id")

        last_run_at = isoparse(d.pop("lastRunAt"))

        model_id = d.pop("modelId")

        primary_key = d.pop("primaryKey")

        referenced_columns = cast(List[str], d.pop("referencedColumns"))

        schedule = SyncSchedule.from_dict(d.pop("schedule"))

        slug = d.pop("slug")

        status = SyncStatus(d.pop("status"))

        updated_at = isoparse(d.pop("updatedAt"))

        workspace_id = d.pop("workspaceId")

        sync = cls(
            configuration=configuration,
            created_at=created_at,
            destination_id=destination_id,
            disabled=disabled,
            id=id,
            last_run_at=last_run_at,
            model_id=model_id,
            primary_key=primary_key,
            referenced_columns=referenced_columns,
            schedule=schedule,
            slug=slug,
            status=status,
            updated_at=updated_at,
            workspace_id=workspace_id,
        )

        sync.additional_properties = d
        return sync

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