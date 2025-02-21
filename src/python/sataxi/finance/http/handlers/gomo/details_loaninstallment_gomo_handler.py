from marshmallow_dataclass import class_schema

from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema
from sataxi.finance.common.instalment_breakdown_lookup import get_gomo_loaninstallment

from bbdcommon.spechelpers.misc import (
    api_response,
    api_validate,
    api_parameter,
    fields,
    ParamLocation,
)
from sataxi.finance.common.schemas.vg_details_loaninstallment_gomo import (
    VGDetailsLoanInstallmentGomoResponse,
)


class VGDetailsLoanInstallmentGomoHandler(DBHandlerBase):
    @api_description("Endpoint for VG Details Loan Installments Gomo Data")
    @api_tag("Gomo")
    @api_parameter(
        "account_number",
        "The Account Number",
        fields.String(required=False),
        location=ParamLocation.Path,
    )
    @api_response(
        None, 200, "Installments", VGDetailsLoanInstallmentGomoResponse, many=True
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 500, "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("gomo.fin.read", required_scopes=["gomo.fin"])
    def get(self, account_number):
        session = self.sessions["Gomo"]
        res = get_gomo_loaninstallment(session, account_number)
        self.finish(
            class_schema(VGDetailsLoanInstallmentGomoResponse)(many=True).dump(res)
        )
