import tornado.httpclient
from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import (
    api_request,
    api_response,
    api_validate,
    class_schema,
)
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema

from sataxi.finance.common.acquire_service import (
    acquire_statement,
    acquire_settlement,
    acquire_notice_settlement,
    acquire_insurance_claim,
)
from sataxi.finance.common.schemas.acquire_schema import (
    SettlementRequest,
    SettlementResponse,
    NoticeSettlementRequest,
    StatementRequest,
    StatementResponse,
    NoticeSettlementResponse,
    InsuranceClaimRequest,
    InsuranceClaimResponse,
)


class AcquireStatement(DBHandlerBase):
    @api_description("Acquire statement generated by Sataxi's Acquire system")
    @api_tag("Acquire")
    @api_request(None, "Statement body", StatementRequest)
    @api_response(None, "200", "successful description", StatementResponse, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 404, "Requested data does not exist.", FailedResponseSchema)
    @api_response(None, 500, "GenericFailure.", FailedResponseSchema)
    @api_validate()  # validates the client_id of the user logged in
    @authorized("sat.fin.stmnt.write", required_scopes=["sat.fin"])
    async def post(self, body: StatementRequest):
        self.logger.info(f"Acquire Statement Request {body.__dict__}")
        if body.account_number.strip() == "" or body.case_number == "":
            raise tornado.httpclient.HTTPError(
                400, "There are values missing in the payload."
            )
        session = self.sessions["HiveRepository"]
        response: StatementResponse = await acquire_statement(
            session, self.application, body, self.current_user
        )
        self.finish(class_schema(StatementResponse)().dump(response))


class AcquireSettlement(DBHandlerBase):
    @api_description("Acquire quote generated by Sataxi's Acquire system")
    @api_tag("Acquire")
    @api_request(None, "Quote body", SettlementRequest)
    @api_response(None, "200", "successful description", SettlementResponse, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 404, "Requested data does not exist.", FailedResponseSchema)
    @api_response(None, 500, "GenericFailure.", FailedResponseSchema)
    @api_validate()  # validates the client_id of the user logged in
    @authorized("sat.fin.stmnt.write", required_scopes=["sat.fin"])
    async def post(self, body: SettlementRequest):
        self.logger.info(f"Acquire Settlement Request {body.__dict__}")
        if body.deal_number == "" or body.settlement_type == "":
            raise tornado.httpclient.HTTPError(
                400, "The Deal Number and Settlement Type cannot be empty!"
            )
        session = self.sessions["HiveRepository"]
        response: SettlementResponse = await acquire_settlement(
            session, self.application, body, self.current_user
        )
        self.finish(class_schema(SettlementResponse)().dump(response))


class AcquireNoticeSettlement(DBHandlerBase):
    @api_description("Acquire quote generated by Sataxi's Acquire system")
    @api_tag("Acquire")
    @api_request(None, "Notice Date body", NoticeSettlementRequest)
    @api_response(
        None, "200", "successful description", NoticeSettlementResponse, many=False
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 404, "Requested data does not exist.", FailedResponseSchema)
    @api_response(None, 500, "GenericFailure.", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.stmnt.write", required_scopes=["sat.fin"])
    async def post(self, body: NoticeSettlementRequest):
        self.logger.info(f"Acquire Notice Settlement Request {body.__dict__}")
        if body.account_number == "":
            raise tornado.httpclient.HTTPError(
                400,
                "BAD REQUEST 400: The Deal Number and Settlement Type cannot be empty!",
            )
        response = await acquire_notice_settlement(self.application, body)
        self.logger.info(f"Acquire Notice Settlement Response {response.__dict__}")
        self.finish(class_schema(NoticeSettlementResponse)().dump(response))


class AcquireInsuranceClaim(DBHandlerBase):
    @api_description("Acquire insurance claim generated by Sataxi's Acquire system")
    @api_tag("Acquire")
    @api_request(None, "Claim body", InsuranceClaimRequest)
    @api_response(
        None, "200", "successful description", InsuranceClaimResponse, many=False
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 404, "Requested data does not exist.", FailedResponseSchema)
    @api_response(None, 500, "GenericFailure.", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.stmnt.write", required_scopes=["sat.fin"])
    async def post(self, body: InsuranceClaimRequest):
        self.logger.info(f"Acquire Insurance Claim Request {body.__dict__}")
        if body.account_number == "" or body.account_number == "":
            raise tornado.httpclient.HTTPError(
                400,
                "BAD REQUEST 400: The Deal Number and Settlement Type cannot be empty!",
            )
        response = await acquire_insurance_claim(
            self.sessions["HiveRepository"], self.application, body, self.current_user
        )
        self.logger.info(f"Acquire Insurance Claim Response {response.__dict__}")
        self.finish(class_schema(InsuranceClaimResponse)().dump(response))
