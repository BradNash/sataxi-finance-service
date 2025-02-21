import json

from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import (
    ParamLocation,
    api_parameter,
    api_response,
    api_validate,
)
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema
from marshmallow import fields
from marshmallow_dataclass import class_schema

from sataxi.finance.common.lookup.location_service import (
    get_all_areas,
    get_all_countries,
    get_area_by_name,
    get_country_by_name,
)
from sataxi.finance.db.sqlalchemy.db_Area import (
    DB_AreaSelectAll,
    DB_AreaSelectByAreaName,
)
from sataxi.finance.db.sqlalchemy.db_Country import (
    DB_CountrySelectAll,
    DB_CountrySelectByCountryName,
)

"""
AREA
"""


class GetAllAreas(DBHandlerBase):
    @api_description("Get All Areas ")
    @api_tag("Lookup")
    @api_response(None, "200", "Areas", DB_AreaSelectAll, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_areas(self.session)
        dc = class_schema(DB_AreaSelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetAreaByName(DBHandlerBase):
    @api_description("Get Area")
    @api_tag("Lookup")
    @api_parameter(
        "area_name",
        "Area Name",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(None, "200", "Area", DB_AreaSelectByAreaName, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, area_name: str):
        res = get_area_by_name(self.session, area_name)
        dc = class_schema(DB_AreaSelectByAreaName)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


"""
COUNTRY
"""


class GetAllCountries(DBHandlerBase):
    @api_description("Get All Countries")
    @api_tag("Lookup")
    @api_response(None, "200", "Countries", DB_CountrySelectAll, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_countries(self.session)
        dc = class_schema(DB_CountrySelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetCountryByName(DBHandlerBase):
    @api_description("Get Country")
    @api_tag("Lookup")
    @api_parameter(
        "country_name",
        "Country Name",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(None, "200", "Country", DB_CountrySelectByCountryName, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, country_name: str):
        res = get_country_by_name(self.session, country_name)
        dc = class_schema(DB_CountrySelectByCountryName)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)
