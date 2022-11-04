import datetime
from typing import Any, Dict, List, Type, TypeVar

from dateutil.parser import isoparse
from pydantic import BaseModel, Field

from ..models.source_configuration import SourceConfiguration
from ..types import UNSET

T = TypeVar("T", bound="Source")


class Source(BaseModel):
    """The database or warehouse where your data is stored. The starting point for
    a Hightouch data pipeline.

        Attributes:
            configuration (SourceConfiguration): The source's configuration. This specifies general metadata about sources,
                like connection details
                Hightouch will use this configuration to connect to underlying source.

                The schema depends on the destination.

                Consumers should NOT make assumptions on the contents of the
                configuration. It may change as Hightouch updates its internal code.
            created_at (datetime.datetime): The timestamp when the source was created
            id (str): The source's id
            name (str): The source's name
            slug (str): The source's slug
            type (str): The source's type (e.g. snowflake or postgres).
            updated_at (datetime.datetime): The timestamp when the source was last updated
            workspace_id (str): The id of the workspace that the source belongs to
    """

    configuration: SourceConfiguration = None
    created_at: datetime.datetime = None
    id: str = None
    name: str = None
    slug: str = None
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
        configuration = SourceConfiguration.from_dict(d.pop("configuration"))

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        type = d.pop("type")

        updated_at = isoparse(d.pop("updatedAt"))

        workspace_id = d.pop("workspaceId")

        source = cls(
            configuration=configuration,
            created_at=created_at,
            id=id,
            name=name,
            slug=slug,
            type=type,
            updated_at=updated_at,
            workspace_id=workspace_id,
        )

        source.additional_properties = d
        return source

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
