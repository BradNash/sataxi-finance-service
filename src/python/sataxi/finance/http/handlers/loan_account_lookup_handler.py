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
from tornado.web import HTTPError

from sataxi.finance.common.loan_account_lookup import (
    get_loan_accounts,
    get_loan_details,
    get_collect_smart_client_details,
)
from sataxi.finance.common.schemas.collect_smart_schema import (
    CollectSmartClientDetailsResponse,
)
from sataxi.finance.common.schemas.loan_schema import (
    LoanAccountLookupResponse,
    LoanDetailsLookupResponse,
)


class LoanAccountLookup(DBHandlerBase):
    @api_description("Get Client Account with ID or Account Number")
    @api_tag("Hive")
    @api_parameter(
        "account_number",
        "The Account Number",
        fields.String(required=False),
        location=ParamLocation.Query,
    )
    @api_parameter(
        "id_number",
        "The IDNumber",
        fields.String(required=False),
        location=ParamLocation.Query,
    )
    @api_response(None, "200", "Accounts", LoanAccountLookupResponse, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, account_number: str, id_number: str):
        session = self.sessions["HiveRepository"]
        res = get_loan_accounts(session, account_number, id_number)
        self.finish(class_schema(LoanAccountLookupResponse)(many=True).dump(res))


class LoanAccountDetailLookup(DBHandlerBase):
    @api_description("Get Client Account Details")
    @api_tag("Hive")
    @api_parameter(
        "account_number",
        "The Account Number",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(None, 200, "Account Details", LoanDetailsLookupResponse, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 500, "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, account_number: str):
        session = self.sessions["HiveRepository"]
        if not account_number:
            raise HTTPError(400, "ACCOUNT NUMBER AND ID NUMBER CANNOT BE EMPTY")
        res = get_loan_details(session, account_number)
        self.finish(class_schema(LoanDetailsLookupResponse)(many=True).dump(res))


class GetCollectSmartClientDetails(DBHandlerBase):
    @api_description("Get Collect Smart Client Details")
    @api_tag("Hive")
    @api_parameter(
        "account_number",
        "The Account Number",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(
        None, "200", "Account Details", CollectSmartClientDetailsResponse, many=False
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, account_number: str):
        if len(account_number.strip()) == 0:
            raise HTTPError(status_code=400, reason="The account number is invalid")
        self.logger.info(f"REQUEST: Account Number - {account_number}")
        hive_session = self.sessions["HiveRepository"]
        response = get_collect_smart_client_details(hive_session, account_number)
        if response is None:
            self.logger.debug("RESPONSE: Null")
        else:
            self.logger.debug(f"RESPONSE: {response.__dict__}")
        self.finish(class_schema(CollectSmartClientDetailsResponse)().dump(response))
