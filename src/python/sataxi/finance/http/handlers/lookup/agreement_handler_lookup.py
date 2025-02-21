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

from sataxi.finance.common.lookup.agreement_service import (
    get_agreement_by_description,
    get_all_agreements,
)
from sataxi.finance.db.sqlalchemy.db_Agreement import (
    DB_AgreementSelectAll,
    DB_AgreementSelectByDescription,
)


class GetAllAgreements(DBHandlerBase):
    @api_description("Get All Agreements")
    @api_tag("Lookup")
    @api_response(None, "200", "Agreement ", DB_AgreementSelectAll, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_agreements(self.session)
        dc = class_schema(DB_AgreementSelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetAgreementByDescription(DBHandlerBase):
    @api_description("Get Agreement by Agreement")
    @api_tag("Lookup")
    @api_parameter(
        "agreement",
        "Agreement",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(
        None, "200", "Agreement ", DB_AgreementSelectByDescription, many=False
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, agreement: str):
        self.logger.info("AGREEMENT : %s", json.dumps({"Agreement": agreement}))
        res = get_agreement_by_description(self.session, agreement)
        dc = class_schema(DB_AgreementSelectByDescription)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)
