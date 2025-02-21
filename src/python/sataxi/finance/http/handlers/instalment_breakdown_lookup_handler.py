from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import (
    api_response,
    api_validate,
    api_parameter,
    ParamLocation,
)
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema
from marshmallow import fields
from marshmallow_dataclass import class_schema

from sataxi.finance.common.instalment_breakdown_lookup import get_instalment_breakdown
from sataxi.finance.common.schemas.instalment_breakdown_schema import (
    InstalmentBreakdownLookUpResponse,
)


class InstalmentBreakdownLookUp(DBHandlerBase):
    @api_description(
        "Accepts a customer Account Number and returns instalment breakdown details"
    )
    @api_tag("Hive")
    @api_parameter(
        "account_number",
        "The Account Number",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(
        None,
        "200",
        "Returns Instalment Breakdown Details",
        InstalmentBreakdownLookUpResponse,
        many=True,
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, account_number: str):
        session = self.sessions["HiveRepository"]
        res = get_instalment_breakdown(session, account_number)
        self.finish(
            class_schema(InstalmentBreakdownLookUpResponse)(many=True).dump(res)
        )
