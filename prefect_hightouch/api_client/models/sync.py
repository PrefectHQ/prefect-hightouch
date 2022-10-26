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
            id (str): The sync's id
            slug (str): The sync's slug
            workspace_id (str): The id of the workspace that the sync belongs to
            created_at (datetime.datetime): The timestamp when the sync was created
            updated_at (datetime.datetime): The timestamp when the sync was last updated
            destination_id (str): The id of the Destination that sync is connected to
            model_id (str): The id of the Model that sync is connected to
            configuration (SyncConfiguration): The sync's configuration. This specifies how data is mapped, among other
                configuration.

                The schema depends on the destination.

                Consumers should NOT make assumptions on the contents of the
                configuration. It may change as Hightouch updates its internal code.
            schedule (SyncSchedule): The scheduling configuration. It can be triggerd based on several ways:

                Interval: the sync will be trigged based on certain interval(minutes/hours/days/weeks)

                Cron: the sync will be trigged based on cron expression https://en.wikipedia.org/wiki/Cron.

                Visual: the sync will be trigged based a visual cron configuration on UI

                DBT-cloud: the sync will be trigged based on a dbt cloud job
            status (SyncStatus):
            disabled (bool): Whether the sync has been disabled by the user.
            last_run_at (datetime.datetime): The timestamp of the last sync run
            referenced_columns (List[str]): The reference column that sync depends on to sync data from source
            primary_key (str): The primary key that sync uses to identify data from source
    """

    id: str
    slug: str
    workspace_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    destination_id: str
    model_id: str
    configuration: SyncConfiguration
    schedule: SyncSchedule
    status: SyncStatus
    disabled: bool
    last_run_at: datetime.datetime
    referenced_columns: List[str]
    primary_key: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        slug = self.slug
        workspace_id = self.workspace_id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        destination_id = self.destination_id
        model_id = self.model_id
        configuration = self.configuration.to_dict()

        schedule = self.schedule.to_dict()

        status = self.status.value

        disabled = self.disabled
        last_run_at = self.last_run_at.isoformat()

        referenced_columns = self.referenced_columns

        primary_key = self.primary_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "workspaceId": workspace_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "destinationId": destination_id,
                "modelId": model_id,
                "configuration": configuration,
                "schedule": schedule,
                "status": status,
                "disabled": disabled,
                "lastRunAt": last_run_at,
                "referencedColumns": referenced_columns,
                "primaryKey": primary_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        slug = d.pop("slug")

        workspace_id = d.pop("workspaceId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        destination_id = d.pop("destinationId")

        model_id = d.pop("modelId")

        configuration = SyncConfiguration.from_dict(d.pop("configuration"))

        schedule = SyncSchedule.from_dict(d.pop("schedule"))

        status = SyncStatus(d.pop("status"))

        disabled = d.pop("disabled")

        last_run_at = isoparse(d.pop("lastRunAt"))

        referenced_columns = cast(List[str], d.pop("referencedColumns"))

        primary_key = d.pop("primaryKey")

        sync = cls(
            id=id,
            slug=slug,
            workspace_id=workspace_id,
            created_at=created_at,
            updated_at=updated_at,
            destination_id=destination_id,
            model_id=model_id,
            configuration=configuration,
            schedule=schedule,
            status=status,
            disabled=disabled,
            last_run_at=last_run_at,
            referenced_columns=referenced_columns,
            primary_key=primary_key,
        )

        sync.additional_properties = d
        return sync

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
