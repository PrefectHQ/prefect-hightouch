import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.model_custom import ModelCustom
from ..models.model_dbt import ModelDbt
from ..models.model_raw import ModelRaw
from ..models.model_table import ModelTable
from ..models.model_tags import ModelTags
from ..models.model_visual import ModelVisual
from ..types import UNSET, Unset

T = TypeVar("T", bound="Model")


@attr.s(auto_attribs=True)
class Model:
    """The SQL query that pulls data from your source to send to your destination.
    We send your SQL query directly to your source so any SQL that is valid for your source (including functions) is
    valid in Hightouch.

        Attributes:
            id (str): The id of the model
            name (str): The name of the model
            slug (str): The slug of the model
            workspace_id (str): The id of the workspace where the model belongs to
            primary_key (str): The primary key will be null if the query doesn't get directly synced (e.g. a relationship
                table for visual querying)
            created_at (datetime.datetime): The timestamp when model was created
            updated_at (datetime.datetime): The timestamp when model was lastly updated
            source_id (str): The id of the source that model is connected to
            query_type (str): The type of the query. Available options: custom, raw_sql, tabel, dbt and visual.
            tags (ModelTags): The tags of the model
            is_schema (bool): If is_schema is true, the model is just used to build other models.
                Either as part of visual querying, or as the root of a visual query.
            syncs (List[str]): The list of id of syncs that uses this model
            visual (Union[Unset, ModelVisual]): Visual query, used by audience
            custom (Union[Unset, ModelCustom]): Custom query for sources that doesn't support sql. For example, Airtable.
            table (Union[Unset, ModelTable]): Table-based query that fetches on a table instead of SQL
            dbt (Union[Unset, ModelDbt]): Query that is based on a dbt model
            raw (Union[Unset, ModelRaw]): Standard raw SQL query
    """

    id: str
    name: str
    slug: str
    workspace_id: str
    primary_key: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    source_id: str
    query_type: str
    tags: ModelTags
    is_schema: bool
    syncs: List[str]
    visual: Union[Unset, ModelVisual] = UNSET
    custom: Union[Unset, ModelCustom] = UNSET
    table: Union[Unset, ModelTable] = UNSET
    dbt: Union[Unset, ModelDbt] = UNSET
    raw: Union[Unset, ModelRaw] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        slug = self.slug
        workspace_id = self.workspace_id
        primary_key = self.primary_key
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        source_id = self.source_id
        query_type = self.query_type
        tags = self.tags.to_dict()

        is_schema = self.is_schema
        syncs = self.syncs

        visual: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.visual, Unset):
            visual = self.visual.to_dict()

        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        table: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.table, Unset):
            table = self.table.to_dict()

        dbt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dbt, Unset):
            dbt = self.dbt.to_dict()

        raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.raw, Unset):
            raw = self.raw.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "workspaceId": workspace_id,
                "primaryKey": primary_key,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "sourceId": source_id,
                "queryType": query_type,
                "tags": tags,
                "isSchema": is_schema,
                "syncs": syncs,
            }
        )
        if visual is not UNSET:
            field_dict["visual"] = visual
        if custom is not UNSET:
            field_dict["custom"] = custom
        if table is not UNSET:
            field_dict["table"] = table
        if dbt is not UNSET:
            field_dict["dbt"] = dbt
        if raw is not UNSET:
            field_dict["raw"] = raw

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        workspace_id = d.pop("workspaceId")

        primary_key = d.pop("primaryKey")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        source_id = d.pop("sourceId")

        query_type = d.pop("queryType")

        tags = ModelTags.from_dict(d.pop("tags"))

        is_schema = d.pop("isSchema")

        syncs = cast(List[str], d.pop("syncs"))

        _visual = d.pop("visual", UNSET)
        visual: Union[Unset, ModelVisual]
        if isinstance(_visual, Unset):
            visual = UNSET
        else:
            visual = ModelVisual.from_dict(_visual)

        _custom = d.pop("custom", UNSET)
        custom: Union[Unset, ModelCustom]
        if isinstance(_custom, Unset):
            custom = UNSET
        else:
            custom = ModelCustom.from_dict(_custom)

        _table = d.pop("table", UNSET)
        table: Union[Unset, ModelTable]
        if isinstance(_table, Unset):
            table = UNSET
        else:
            table = ModelTable.from_dict(_table)

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

        model = cls(
            id=id,
            name=name,
            slug=slug,
            workspace_id=workspace_id,
            primary_key=primary_key,
            created_at=created_at,
            updated_at=updated_at,
            source_id=source_id,
            query_type=query_type,
            tags=tags,
            is_schema=is_schema,
            syncs=syncs,
            visual=visual,
            custom=custom,
            table=table,
            dbt=dbt,
            raw=raw,
        )

        model.additional_properties = d
        return model

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
