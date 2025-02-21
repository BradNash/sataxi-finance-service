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

from sataxi.finance.common.lookup.client_type_service import (
    get_all_client_types,
    get_client_type_by_type,
)
from sataxi.finance.db.sqlalchemy.db_ClientType import (
    DB_ClientTypeSelectAll,
    DB_ClientTypeSelectByType,
)


class GetAllClientTypes(DBHandlerBase):
    @api_description("Get All ClientTypes")
    @api_tag("Lookup")
    @api_response(None, "200", "Client Types", DB_ClientTypeSelectAll, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_client_types(self.session)
        dc = class_schema(DB_ClientTypeSelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetClientTypeByType(DBHandlerBase):
    @api_description("Get Client  Type by Client Type")
    @api_tag("Lookup")
    @api_parameter(
        "client_type",
        "Client Type",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(
        None, "200", "Client  Type Type", DB_ClientTypeSelectByType, many=False
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, client_type: str):
        self.logger.info("CLIENT TYPE: %s", json.dumps({"Client Type": client_type}))
        res = get_client_type_by_type(self.session, client_type)
        dc = class_schema(DB_ClientTypeSelectByType)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)
