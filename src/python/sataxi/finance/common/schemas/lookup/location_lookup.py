from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class CountryLookupResponse:
    country_id: int = schema_field(data_key="countryID", required=True)
    country_name: str = schema_field(data_key="countryName", required=True)


@dataclass
class AreaLookupResponse:
    area_id: int = schema_field(data_key="areaID", required=True)
    area_name: str = schema_field(data_key="areaName", required=True)
