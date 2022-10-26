import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..models.destination_configuration import DestinationConfiguration

T = TypeVar("T", bound="Destination")


@attr.s(auto_attribs=True)
class Destination:
    """The service receiving your data (e.g. Salesforce, Hubspot, Customer.io, or a
    SFTP server)

        Attributes:
            id (str): The destination's id
            name (str): The destination's name
            slug (str): The destination's slug
            workspace_id (str): The id of the workspace that the destination belongs to
            created_at (datetime.datetime): The timestamp when the destination was created
            updated_at (datetime.datetime): The timestamp when the destination was last updated
            type (str): The destination's type (e.g. salesforce or hubspot).
            configuration (DestinationConfiguration): The destination's configuration. This specifies general metadata about
                destination, like hostname and username.
                Hightouch will be using this configuration to connect to destination.

                The schema depends on the destination.

                Consumers should NOT make assumptions on the contents of the
                configuration. It may change as Hightouch updates its internal code.
            syncs (List[str]): A list of syncs that sync to this destination.
    """

    id: str
    name: str
    slug: str
    workspace_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    type: str
    configuration: DestinationConfiguration
    syncs: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        slug = self.slug
        workspace_id = self.workspace_id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        type = self.type
        configuration = self.configuration.to_dict()

        syncs = self.syncs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "workspaceId": workspace_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "type": type,
                "configuration": configuration,
                "syncs": syncs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        workspace_id = d.pop("workspaceId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        type = d.pop("type")

        configuration = DestinationConfiguration.from_dict(d.pop("configuration"))

        syncs = cast(List[str], d.pop("syncs"))

        destination = cls(
            id=id,
            name=name,
            slug=slug,
            workspace_id=workspace_id,
            created_at=created_at,
            updated_at=updated_at,
            type=type,
            configuration=configuration,
            syncs=syncs,
        )

        destination.additional_properties = d
        return destination

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
