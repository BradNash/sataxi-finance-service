from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class RelationLookupResponse:
    relation_id: int = schema_field(data_key="relationID", required=True)
    relation: str = schema_field(data_key="relation", required=True)
