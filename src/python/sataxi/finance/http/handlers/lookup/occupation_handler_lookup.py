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

from sataxi.finance.common.lookup.occupation_service import (
    get_all_occupations,
    get_occupation_by_occupation,
)
from sataxi.finance.db.sqlalchemy.db_Occupation import (
    DB_OccupationSelectAll,
    DB_OccupationSelectByOccupation,
)


class GetAllOccupations(DBHandlerBase):
    @api_description("Get All Occupations")
    @api_tag("Lookup")
    @api_response(None, "200", "Occupations", DB_OccupationSelectAll, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_occupations(self.session)
        dc = class_schema(DB_OccupationSelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetOccupationByOccupation(DBHandlerBase):
    @api_description("Get Occupation by Occupation")
    @api_tag("Lookup")
    @api_parameter(
        "occupation",
        "Occupation",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(
        None, "200", "Occupation", DB_OccupationSelectByOccupation, many=False
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, occupation: str):
        res = get_occupation_by_occupation(self.session, occupation)
        dc = class_schema(DB_OccupationSelectByOccupation)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)
