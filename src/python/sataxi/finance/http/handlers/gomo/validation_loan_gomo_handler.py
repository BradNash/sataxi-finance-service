import tornado

from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import (
    api_response,
    api_parameter,
    fields,
    ParamLocation,
)
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema
from marshmallow_dataclass import class_schema
from sataxi.finance.common.loan_account_lookup import get_gomo_validation_loan_accounts
from sataxi.finance.common.schemas.vg_validation_loan_gomo import (
    VGValidationLoanGomoResponse,
)


class VGValidationLoanGomoHandler(DBHandlerBase):
    @api_description("Endpoint for VG Validation Loan Gomo Data")
    @api_tag("Gomo")
    @api_parameter(
        "account_number",
        "The Account Number",
        fields.String(required=False),
        location=ParamLocation.Query,
    )
    @api_parameter(
        "id_no",
        "The ID Number",
        fields.String(required=False),
        location=ParamLocation.Query,
    )
    @api_response(None, 200, "Accounts", VGValidationLoanGomoResponse, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 500, "Generic Failure", FailedResponseSchema)
    # @api_validate()
    # @authorized("gomo.fin.read", required_scopes=["gomo.fin"])
    def get(self, account_number: str, id_no: str):
        session = self.sessions["Gomo"]
        if account_number is None and id_no is None:
            raise tornado.httpclient.HTTPError(
                400, "Account Number or ID Number required"
            )
        res = get_gomo_validation_loan_accounts(
            session, account_number=account_number, id_no=id_no
        )
        self.finish(class_schema(VGValidationLoanGomoResponse)(many=True).dump(res))
