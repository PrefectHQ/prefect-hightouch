import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from dateutil.parser import isoparse
from pydantic import BaseModel, Field

from ..models.model_custom import ModelCustom
from ..models.model_dbt import ModelDbt
from ..models.model_raw import ModelRaw
from ..models.model_table import ModelTable
from ..models.model_tags import ModelTags
from ..models.model_visual import ModelVisual
from ..types import UNSET, Unset

T = TypeVar("T", bound="Model")


class Model(BaseModel):
    """The SQL query that pulls data from your source to send to your destination.
    We send your SQL query directly to your source so any SQL that is valid for your source (including functions) is
    valid in Hightouch.

        Attributes:
            created_at (datetime.datetime): The timestamp when model was created
            id (str): The id of the model
            is_schema (bool): If is_schema is true, the model is just used to build other models.
                Either as part of visual querying, or as the root of a visual query.
            name (str): The name of the model
            primary_key (str): The primary key will be null if the query doesn't get directly synced (e.g. a relationship
                table for visual querying)
            query_type (str): The type of the query. Available options: custom, raw_sql, tabel, dbt and visual.
            slug (str): The slug of the model
            source_id (str): The id of the source that model is connected to
            syncs (List[str]): The list of id of syncs that uses this model
            tags (ModelTags): The tags of the model
            updated_at (datetime.datetime): The timestamp when model was lastly updated
            workspace_id (str): The id of the workspace where the model belongs to
            custom (Union[Unset, ModelCustom]): Custom query for sources that doesn't support sql. For example, Airtable.
            dbt (Union[Unset, ModelDbt]): Query that is based on a dbt model
            raw (Union[Unset, ModelRaw]): Standard raw SQL query
            table (Union[Unset, ModelTable]): Table-based query that fetches on a table instead of SQL
            visual (Union[Unset, ModelVisual]): Visual query, used by audience
    """

    created_at: datetime.datetime = None
    id: str = None
    is_schema: bool = None
    name: str = None
    primary_key: str = None
    query_type: str = None
    slug: str = None
    source_id: str = None
    syncs: List[str] = None
    tags: ModelTags = None
    updated_at: datetime.datetime = None
    workspace_id: str = None
    custom: Union[Unset, ModelCustom] = UNSET
    dbt: Union[Unset, ModelDbt] = UNSET
    raw: Union[Unset, ModelRaw] = UNSET
    table: Union[Unset, ModelTable] = UNSET
    visual: Union[Unset, ModelVisual] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id
        is_schema = self.is_schema
        name = self.name
        primary_key = self.primary_key
        query_type = self.query_type
        slug = self.slug
        source_id = self.source_id
        syncs = self.syncs

        tags = self.tags.to_dict()

        updated_at = self.updated_at.isoformat()

        workspace_id = self.workspace_id
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        dbt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dbt, Unset):
            dbt = self.dbt.to_dict()

        raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.raw, Unset):
            raw = self.raw.to_dict()

        table: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.table, Unset):
            table = self.table.to_dict()

        visual: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.visual, Unset):
            visual = self.visual.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "isSchema": is_schema,
                "name": name,
                "primaryKey": primary_key,
                "queryType": query_type,
                "slug": slug,
                "sourceId": source_id,
                "syncs": syncs,
                "tags": tags,
                "updatedAt": updated_at,
                "workspaceId": workspace_id,
            }
        )
        if custom is not UNSET:
            field_dict["custom"] = custom
        if dbt is not UNSET:
            field_dict["dbt"] = dbt
        if raw is not UNSET:
            field_dict["raw"] = raw
        if table is not UNSET:
            field_dict["table"] = table
        if visual is not UNSET:
            field_dict["visual"] = visual

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        is_schema = d.pop("isSchema")

        name = d.pop("name")

        primary_key = d.pop("primaryKey")

        query_type = d.pop("queryType")

        slug = d.pop("slug")

        source_id = d.pop("sourceId")

        syncs = cast(List[str], d.pop("syncs"))

        tags = ModelTags.from_dict(d.pop("tags"))

        updated_at = isoparse(d.pop("updatedAt"))

        workspace_id = d.pop("workspaceId")

        _custom = d.pop("custom", UNSET)
        custom: Union[Unset, ModelCustom]
        if isinstance(_custom, Unset):
            custom = UNSET
        else:
            custom = ModelCustom.from_dict(_custom)

        _dbt = d.pop("dbt", UNSET)
        dbt: Union[Unset, ModelDbt]
        if isinstance(_dbt, Unset):
            dbt = UNSET
        else:
            dbt = ModelDbt.from_dict(_dbt)

        _raw = d.pop("raw", UNSET)
        raw: Union[Unset, ModelRaw]
        if isinstance(_raw, Unset):
            raw = UNSET
        else:
            raw = ModelRaw.from_dict(_raw)

        _table = d.pop("table", UNSET)
        table: Union[Unset, ModelTable]
        if isinstance(_table, Unset):
            table = UNSET
        else:
            table = ModelTable.from_dict(_table)

        _visual = d.pop("visual", UNSET)
        visual: Union[Unset, ModelVisual]
        if isinstance(_visual, Unset):
            visual = UNSET
        else:
            visual = ModelVisual.from_dict(_visual)

        model = cls(
            created_at=created_at,
            id=id,
            is_schema=is_schema,
            name=name,
            primary_key=primary_key,
            query_type=query_type,
            slug=slug,
            source_id=source_id,
            syncs=syncs,
            tags=tags,
            updated_at=updated_at,
            workspace_id=workspace_id,
            custom=custom,
            dbt=dbt,
            raw=raw,
            table=table,
            visual=visual,
        )

        model.additional_properties = d
        return model

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
