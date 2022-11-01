import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

from dateutil.parser import isoparse
from pydantic import BaseModel, Field

from ..models.destination_configuration import DestinationConfiguration
from ..types import UNSET

T = TypeVar("T", bound="Destination")


class Destination(BaseModel):
    """The service receiving your data (e.g. Salesforce, Hubspot, Customer.io, or a
    SFTP server)

        Attributes:
            configuration (DestinationConfiguration): The destination's configuration. This specifies general metadata about
                destination, like hostname and username.
                Hightouch will be using this configuration to connect to destination.

                The schema depends on the destination.

                Consumers should NOT make assumptions on the contents of the
                configuration. It may change as Hightouch updates its internal code.
            created_at (datetime.datetime): The timestamp when the destination was created
            id (str): The destination's id
            name (str): The destination's name
            slug (str): The destination's slug
            syncs (List[str]): A list of syncs that sync to this destination.
            type (str): The destination's type (e.g. salesforce or hubspot).
            updated_at (datetime.datetime): The timestamp when the destination was last updated
            workspace_id (str): The id of the workspace that the destination belongs to
    """

    configuration: DestinationConfiguration = None
    created_at: datetime.datetime = None
    id: str = None
    name: str = None
    slug: str = None
    syncs: List[str] = None
    type: str = None
    updated_at: datetime.datetime = None
    workspace_id: str = None
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        configuration = self.configuration.to_dict()

        created_at = self.created_at.isoformat()

        id = self.id
        name = self.name
        slug = self.slug
        syncs = self.syncs

        type = self.type
        updated_at = self.updated_at.isoformat()

        workspace_id = self.workspace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "createdAt": created_at,
                "id": id,
                "name": name,
                "slug": slug,
                "syncs": syncs,
                "type": type,
                "updatedAt": updated_at,
                "workspaceId": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        configuration = DestinationConfiguration.from_dict(d.pop("configuration"))

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        syncs = cast(List[str], d.pop("syncs"))

        type = d.pop("type")

        updated_at = isoparse(d.pop("updatedAt"))

        workspace_id = d.pop("workspaceId")

        destination = cls(
            configuration=configuration,
            created_at=created_at,
            id=id,
            name=name,
            slug=slug,
            syncs=syncs,
            type=type,
            updated_at=updated_at,
            workspace_id=workspace_id,
        )

        destination.additional_properties = d
        return destination

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
