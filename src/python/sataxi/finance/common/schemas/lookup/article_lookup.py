from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class ArticleTypeLookupResponse:
    type_id: int = schema_field(data_key="typeID", required=True)
    type: str = schema_field(data_key="type", required=True)
