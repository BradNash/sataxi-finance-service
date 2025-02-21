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

from sataxi.finance.db.sqlalchemy.db_DealerCode import (
    DB_DealerCodeSelectAll,
    DB_DealerCodeSelectByCode,
)
from ....common.lookup.dealer_code_service import (
    get_all_dealer_codes,
    get_dealer_code_by_code,
)


class GetAllDealerCodes(DBHandlerBase):
    @api_description("Get All Dealer Codes")
    @api_tag("Lookup")
    @api_response(None, "200", "Dealer Codes", DB_DealerCodeSelectAll, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_dealer_codes(self.session)
        dc = class_schema(DB_DealerCodeSelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetDealerCodeByCode(DBHandlerBase):
    @api_description("Get Dealer Code by Code")
    @api_tag("Lookup")
    @api_parameter(
        "dealer_code",
        "Dealer Code",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(None, "200", "Dealer Code", DB_DealerCodeSelectByCode, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, dealer_code: str):
        self.logger.info("DELALER CODE : %s", json.dumps({"Dealer Code": dealer_code}))
        res = get_dealer_code_by_code(self.session, dealer_code)
        dc = class_schema(DB_DealerCodeSelectByCode)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)
