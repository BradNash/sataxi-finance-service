from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import (
    api_response,
    api_validate,
    api_parameter,
    fields,
    ParamLocation,
)
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema
from marshmallow_dataclass import class_schema
from sataxi.finance.common.gomo_statement_details_service import (
    gomo_get_statement_details,
)

from sataxi.finance.common.schemas.vg_gomo_get_statement_details_schema import (
    VGGomoGetStatementDetailsResponse,
)


class VGGomoGetStatementDetailsHandler(DBHandlerBase):
    @api_description("Endpoint for VG Gomo Get Statement Details")
    @api_tag("Gomo")
    @api_parameter(
        "account_number",
        "The Account Number",
        fields.String(required=True),
        location=ParamLocation.Path,
    )
    @api_response(None, 200, "Accounts", VGGomoGetStatementDetailsResponse, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 500, "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("gomo.fin.read", required_scopes=["gomo.fin"])
    def get(self, account_number: str):
        session = self.sessions["Gomo"]
        res = gomo_get_statement_details(session, account_number)
        self.finish(
            class_schema(VGGomoGetStatementDetailsResponse)(many=True).dump(res)
        )
