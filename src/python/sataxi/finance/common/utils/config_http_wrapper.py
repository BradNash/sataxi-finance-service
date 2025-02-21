import json
import logging

from marshmallow_dataclass import class_schema

from sataxi.finance.common.schemas.acquire_schema import (
    SettlementRequest,
    AcquireSettlementRequest,
    SettlementResponse,
    StatementRequest,
    AcquireStatementRequest,
    StatementResponse,
    NoticeSettlementRequest,
    AcquireNoticeSettlementRequest,
    NoticeSettlementResponse,
    InsuranceClaimRequest,
    InsuranceClaimResponse,
    AcquireInsuranceClaimRequest,
)
from sataxi.finance.common.schemas.default_configs import AcquireConfigs, SignioConfigs
from sataxi.finance.common.utils.http_wrapper import HttpWrapper, ReturnType


class ConfigHttpWrapper(HttpWrapper):
    def __init__(self):
        super().__init__({"content-type": "application/json"})

    async def acquire_statement(
        self,
        acquire_configs: AcquireConfigs,
        statement_request: StatementRequest,
        timeout: int,
    ) -> StatementResponse:
        payload = AcquireStatementRequest(
            statement_request.account_number,
            str(statement_request.start_date.strftime(acquire_configs.date_format)),
            acquire_configs.user_id,
            acquire_configs.path,
            acquire_configs.system_id,
            acquire_configs.system_name,
        )

        request_url = acquire_configs.url + "api/GenerateStatement/"
        body = json.dumps(payload.__dict__)

        self.log_request(request_url, body)

        res = await self.send_http_request(
            "POST",
            request_url,
            body,
            timeout,
            ReturnType.BODY,
        )
        statement_response = json.loads(res.decode("utf-8"))
        return StatementResponse(
            statement_response["Path"],
            statement_response["FileName"],
            statement_response["Message"],
            b"",
            "",
        )

    async def acquire_settlement(
        self,
        acquire_configs: AcquireConfigs,
        settlement_request: SettlementRequest,
        timeout: int,
    ) -> SettlementResponse:
        payload = AcquireSettlementRequest(
            settlement_request.deal_number,
            str(settlement_request.settlement_type.value),
            settlement_request.continue_car_track,
            acquire_configs.user_id,
            acquire_configs.path,
            acquire_configs.system_id,
            acquire_configs.period_for_quotation_validity,
        )

        request_url = acquire_configs.url + "api/SettlementAPI/"
        body = json.dumps(payload.__dict__)
        self.log_request(request_url, body)

        res = await self.send_http_request(
            "POST",
            request_url,
            body,
            timeout,
            ReturnType.BODY,
        )
        settlement_response = json.loads(res.decode("utf-8"))
        return SettlementResponse(
            settlement_response["Path"],
            settlement_response["FileName"],
            settlement_response["Message"],
            b"",
            "",
        )

    async def acquire_notice_settlement(
        self,
        acquire_configs: AcquireConfigs,
        notice_settlement_request: NoticeSettlementRequest,
        timeout: int,
    ) -> NoticeSettlementResponse:
        payload = AcquireNoticeSettlementRequest(
            notice_settlement_request.account_number,
            notice_settlement_request.notice_date.strftime("%Y-%m-%d %H:%M:%S"),
            acquire_configs.system_name,
            acquire_configs.system_id,
            acquire_configs.user_id,
        )

        request_url = acquire_configs.url + "api/NoticePeriodSettlementAPI/"
        body = json.dumps(payload.__dict__)

        self.log_request(request_url, body)

        res = await self.send_http_request(
            "POST",
            request_url,
            body,
            timeout,
            ReturnType.BODY,
        )
        acquire_response = json.loads(res.decode("utf-8"))
        return NoticeSettlementResponse(
            acquire_response["Message"],
            acquire_response["NoticeStartDate"],
            acquire_response["NoticeEndDate"],
            acquire_response["RemainingDays"],
        )

    async def acquire_insurance_claim(
        self,
        acquire_configs: AcquireConfigs,
        insurance_claim_request: InsuranceClaimRequest,
        timeout: int,
    ) -> InsuranceClaimResponse:
        payload = class_schema(AcquireInsuranceClaimRequest)().dump(
            AcquireInsuranceClaimRequest(
                insurance_claim_request.account_number,
                str(insurance_claim_request.settlement_type.value),
                insurance_claim_request.continue_car_track,
                acquire_configs.period_for_quotation_validity,
                acquire_configs.system_id,
                acquire_configs.user_id,
                acquire_configs.path,
                insurance_claim_request.legal_fees_payable,
                insurance_claim_request.legal_notes,
                insurance_claim_request.is_ins_settlement,
                acquire_configs.username,
                insurance_claim_request.date_of_loss,
            )
        )

        request_url = acquire_configs.url + "api/INSSettlementAPI/"
        body = json.dumps(payload)
        self.log_request(request_url, body)

        res = await self.send_http_request(
            "POST",
            request_url,
            body,
            timeout,
            ReturnType.BODY,
        )
        insurance_claim_response = json.loads(res.decode("utf-8"))
        return InsuranceClaimResponse(
            insurance_claim_response["Path"],
            insurance_claim_response["FileName"],
            insurance_claim_response["Message"],
            b"",
            "",
        )

    async def submit_3rd_party_application(
        self, signio_configs: SignioConfigs, xml_data: str
    ):
        super().__init__(
            {
                "X-Auth-Token": signio_configs.auth_token,
                "Content-Type": "text/xml",
                "Authorization": signio_configs.authorisation,
            }
        )
        logging.info(f"Signio settlement request payload [{xml_data}]")

        request_url = signio_configs.url + "submit3rdPartyApplication"
        body = xml_data

        # self.log_request(request_url, body)

        res = await self.send_http_request(
            "POST",
            request_url,
            body,
            30,
            ReturnType.FULL,
        )
        logging.info(f"Signio settlement response payload [{res.body.decode('utf-8')}]")
        return res

    @staticmethod
    def log_request(request_url: str, payload: str):
        logging.info(f"Http request to [{request_url}] using payload [{payload}]")
