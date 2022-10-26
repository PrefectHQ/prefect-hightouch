import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.source_configuration import SourceConfiguration

T = TypeVar("T", bound="Source")


@attr.s(auto_attribs=True)
class Source:
    """The database or warehouse where your data is stored. The starting point for
    a Hightouch data pipeline.

        Attributes:
            id (str): The source's id
            name (str): The source's name
            slug (str): The source's slug
            workspace_id (str): The id of the workspace that the source belongs to
            created_at (datetime.datetime): The timestamp when the source was created
            updated_at (datetime.datetime): The timestamp when the source was last updated
            configuration (SourceConfiguration): The source's configuration. This specifies general metadata about sources,
                like connection details
                Hightouch will use this configuration to connect to underlying source.

                The schema depends on the destination.

                Consumers should NOT make assumptions on the contents of the
                configuration. It may change as Hightouch updates its internal code.
            type (str): The source's type (e.g. snowflake or postgres).
    """

    id: str
    name: str
    slug: str
    workspace_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    configuration: SourceConfiguration
    type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        slug = self.slug
        workspace_id = self.workspace_id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        configuration = self.configuration.to_dict()

        type = self.type

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
                "configuration": configuration,
                "type": type,
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

        configuration = SourceConfiguration.from_dict(d.pop("configuration"))

        type = d.pop("type")

        source = cls(
            id=id,
            name=name,
            slug=slug,
            workspace_id=workspace_id,
            created_at=created_at,
            updated_at=updated_at,
            configuration=configuration,
            type=type,
        )

        source.additional_properties = d
        return source

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
