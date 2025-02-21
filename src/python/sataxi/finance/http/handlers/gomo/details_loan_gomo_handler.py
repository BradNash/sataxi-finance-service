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

from sataxi.finance.common.loan_account_lookup import (
    get_gomo_loan_accounts,
)

from sataxi.finance.common.schemas.vg_details_loan_gomo import VGDetailsLoanGomoResponse


class VGDetailsLoanGomoHandler(DBHandlerBase):
    @api_description("Endpoint for VG Details Loan Gomo Data")
    @api_tag("Gomo")
    @api_parameter(
        "account_number",
        "The Account Number",
        fields.String(required=True),
        location=ParamLocation.Path,
    )
    @api_response(None, 200, "Accounts", VGDetailsLoanGomoResponse, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 500, "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("gomo.fin.read", required_scopes=["gomo.fin"])
    def get(self, account_number: str):
        session = self.sessions["Gomo"]
        res = get_gomo_loan_accounts(session, account_number)
        self.finish(class_schema(VGDetailsLoanGomoResponse)(many=True).dump(res))
