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

from sataxi.finance.common.lookup.employment_service import (
    get_all_employer_industry_types,
    get_employer_industry_type_by_type,
)
from sataxi.finance.db.sqlalchemy.db_EmployerIndustryType import (
    DB_EmployerIndustryTypeSelectAll,
    DB_EmployerIndustryTypeSelectByType,
)

"""
EMPLOYER INDUSTRY TYPE
"""


class GetAllEmployerIndustryTypes(DBHandlerBase):
    @api_description("Get All Employer Industry Types ")
    @api_tag("Lookup")
    @api_response(
        None,
        "200",
        "Employer Industry Types",
        DB_EmployerIndustryTypeSelectAll,
        many=True,
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_employer_industry_types(self.session)
        dc = class_schema(DB_EmployerIndustryTypeSelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetEmployerIndustryTypeByType(DBHandlerBase):
    @api_description("Get Employer Industry Type")
    @api_tag("Lookup")
    @api_parameter(
        "industry_type",
        "Employer Industry Type",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(
        None,
        "200",
        "Employer Industry Type",
        DB_EmployerIndustryTypeSelectByType,
        many=False,
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, industry_type: str):
        res = get_employer_industry_type_by_type(self.session, industry_type)
        dc = class_schema(DB_EmployerIndustryTypeSelectByType)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)
