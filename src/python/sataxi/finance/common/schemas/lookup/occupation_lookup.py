from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class OccupationLookupResponse:
    occupation_id: int = schema_field(data_key="occupationID", required=True)
    occupation: str = schema_field(data_key="occupation", required=True)
