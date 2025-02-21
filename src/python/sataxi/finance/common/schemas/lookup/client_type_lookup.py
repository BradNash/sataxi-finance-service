from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class ClientTypeLookupResponse:
    client_id: int = schema_field(data_key="clientTypeID", required=True)
    type: str = schema_field(data_key="type", required=True)
