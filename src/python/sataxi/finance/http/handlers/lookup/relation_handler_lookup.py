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

from sataxi.finance.common.lookup.relation_service import (
    get_all_relations,
    get_relation_by_relative,
)
from sataxi.finance.db.sqlalchemy.db_Relation import (
    DB_RelationSelectAll,
    DB_RelationSelectByRelative,
)


class GetAllRelations(DBHandlerBase):
    @api_description("Get All Relations")
    @api_tag("Lookup")
    @api_response(None, "200", "Relations", DB_RelationSelectAll, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_relations(self.session)
        dc = class_schema(DB_RelationSelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetRelationByRelative(DBHandlerBase):
    @api_description("Get Relation by Relative")
    @api_tag("Lookup")
    @api_parameter(
        "relative",
        "Relative",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(None, "200", "Relation", DB_RelationSelectByRelative, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, relative: str):
        self.logger.info("RELATIVE : %s", json.dumps({"Relative": relative}))
        res = get_relation_by_relative(self.session, relative)
        dc = class_schema(DB_RelationSelectByRelative)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)
