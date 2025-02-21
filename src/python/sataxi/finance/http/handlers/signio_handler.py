from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import (
    api_request,
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
from tornado.web import HTTPError

from sataxi.finance.common.schemas.signio_schema import SignioLoanDetailsRequest
from sataxi.finance.common.signio_loan_service import (
    save_signio_loan_details,
    fetch_loan_details,
    submit_signio_application,
)


class SaveLoanApplication(DBHandlerBase):
    @api_description("Insert the Signio loan details")
    @api_tag("Signio")
    @api_request(None, "Signio body", SignioLoanDetailsRequest)
    @api_response(None, "200", "successful description", many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 500, "GenericFailure.", FailedResponseSchema)
    @api_validate()
    @authorized(
        "sat.fin.stmnt.write", required_scopes=["sat.fin"]
    )  # TODO: need to make own operation change sat.fin.stmnt.write -> sat.fin.write
    # || sat.signio.write/sat.signio.read
    async def post(self, body: SignioLoanDetailsRequest):
        if body.caseNumber is None:
            raise HTTPError(400, "The Case Number cannot be empty!")
        save_signio_loan_details(self.session, body)
        self.finish()


class SubmitLoanApplication(DBHandlerBase):
    @api_description("Insert the Signio loan details")
    @api_tag("Signio")
    @api_request(None, "Signio body", SignioLoanDetailsRequest)
    @api_response(None, "200", "successful description", many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 500, "GenericFailure.", FailedResponseSchema)
    @api_validate()
    @authorized(
        "sat.fin.stmnt.write", required_scopes=["sat.fin"]
    )  # TODO: need to make own operation change sat.fin.stmnt.write -> sat.fin.write
    # || sat.signio.write/sat.signio.read
    async def post(self, body: SignioLoanDetailsRequest):
        self.logger.info(f"Signio Loan Details Request: {body}")

        if body.caseNumber is None:
            raise HTTPError(400, "BAD REQUEST 400: The Case Number cannot be empty!")

        # export_signio_application_to_excel(self.application, body, self.current_user)
        await submit_signio_application(self.session, self.application, body)
        self.finish()


class GetLoanDetails(DBHandlerBase):
    @api_description("GET the Signio loan details payload")
    @api_tag("Signio")
    @api_parameter(
        "id_number",
        "ID Number of Customer",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(
        None, "200", "successful description", SignioLoanDetailsRequest, many=False
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 500, "GenericFailure.", FailedResponseSchema)
    @api_validate()
    @authorized(
        "sat.fin.read", required_scopes=["sat.fin"]
    )  # TODO: need to make own operation sat.signio.write/sat.signio.read
    async def get(self, id_number: str):
        if id_number is None or id_number == "":
            raise HTTPError(400, "BAD REQUEST 400: The Case Number cannot be empty!")
        hive_session = self.sessions["HiveRepository"]
        response = fetch_loan_details(hive_session, id_number)
        self.finish(class_schema(SignioLoanDetailsRequest)().dump(response))
