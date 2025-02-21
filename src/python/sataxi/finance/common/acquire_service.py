import base64
import logging
import tempfile
import uuid
from dataclasses import dataclass

from bbdcommon.tornadohelpers.base.proto import AppProto
from smb.SMBConnection import SMBConnection
from smb.base import SMBTimeout
from sqlalchemy.orm import Session
from tornado.httpclient import HTTPError

from sataxi.finance.common.loan_account_lookup import get_loan_accounts
from sataxi.finance.common.schemas.acquire_schema import (
    SettlementRequest,
    NoticeSettlementRequest,
    StatementRequest,
    DocumentType,
    NoticeSettlementResponse,
    InsuranceClaimRequest,
    InsuranceClaimResponse,
)
from sataxi.finance.common.schemas.default_configs import AcquireConfigs
from sataxi.finance.common.utils.config_http_wrapper import ConfigHttpWrapper
from sataxi.finance.messaging.commands.attach_document import AttachDocumentV1
from sataxi.finance.messaging.events.statement_generated import StatementGeneratedV1


@dataclass
class EventOBJ:
    request: any
    application: AppProto
    case_number: str
    guid: str
    username: str
    document_type: DocumentType
    acquire_configs: AcquireConfigs
    account_number: str
    customer_email: str
    customer_idnumber: str
    customer_name: str


async def acquire_statement(
    session: Session,
    application: AppProto,
    statement_request: StatementRequest,
    current_user: str,
):
    http_wrapper = ConfigHttpWrapper()
    acquire_configs: AcquireConfigs = populate_defaults(application)
    timeout = statement_request.timeout or acquire_configs.timeout
    statement_response = await http_wrapper.acquire_statement(
        acquire_configs, statement_request, timeout
    )
    statement_response.guid = str(uuid.uuid4())
    loan_details = get_loan_accounts(session, statement_request.account_number, "")
    session.commit()
    if len(loan_details) > 0:
        loan_details = loan_details[0]

    event_obj = EventOBJ(
        request=statement_response,
        application=application,
        case_number=statement_request.case_number,
        guid=statement_response.guid,
        username=current_user,
        document_type=DocumentType.STATEMENT,
        acquire_configs=acquire_configs,
        account_number=statement_request.account_number,
        customer_email=statement_request.customer_email,
        customer_idnumber=statement_request.customer_idnumber,
        customer_name=loan_details.customer_name or "Customer",
    )
    await send_event(event_obj)
    return statement_response


async def acquire_settlement(
    session: Session,
    application: AppProto,
    settlement_request: SettlementRequest,
    current_user: str,
):
    acquire_configs: AcquireConfigs = populate_defaults(application)
    timeout = (
        settlement_request.timeout
        if (settlement_request.timeout or settlement_request.timeout != 0)
        else acquire_configs.timeout
    )
    http_wrapper = ConfigHttpWrapper()
    settlement_response = await http_wrapper.acquire_settlement(
        acquire_configs, settlement_request, timeout
    )
    settlement_response.guid = str(uuid.uuid4())
    loan_details = get_loan_accounts(session, settlement_request.deal_number, "")
    session.commit()
    if len(loan_details) > 0:
        loan_details = loan_details[0]

    event_obj = EventOBJ(
        request=settlement_response,
        application=application,
        case_number=settlement_request.case_number,
        guid=settlement_response.guid,
        username=current_user,
        document_type=settlement_request.settlement_type,
        acquire_configs=acquire_configs,
        account_number=settlement_request.deal_number,
        customer_email=settlement_request.customer_email,
        customer_idnumber=settlement_request.customer_idnumber,
        customer_name=loan_details.customer_name or "Customer",
    )

    await send_event(event_obj)
    return settlement_response


async def acquire_notice_settlement(
    application: AppProto, notice_settlement_request: NoticeSettlementRequest
) -> NoticeSettlementResponse:
    acquire_configs: AcquireConfigs = populate_defaults(application)
    timeout = (
        notice_settlement_request.timeout
        if (notice_settlement_request.timeout or notice_settlement_request.timeout != 0)
        else acquire_configs.timeout
    )
    http_wrapper = ConfigHttpWrapper()
    acquire_response = await http_wrapper.acquire_notice_settlement(
        acquire_configs, notice_settlement_request, timeout
    )
    return acquire_response


async def acquire_insurance_claim(
    session: Session,
    application: AppProto,
    insurance_claim_request: InsuranceClaimRequest,
    current_user: str,
) -> InsuranceClaimResponse:
    acquire_configs: AcquireConfigs = populate_defaults(application)
    timeout = (
        insurance_claim_request.timeout
        if (insurance_claim_request.timeout or insurance_claim_request.timeout != 0)
        else acquire_configs.timeout
    )
    http_wrapper = ConfigHttpWrapper()
    insurance_claim_response = await http_wrapper.acquire_insurance_claim(
        acquire_configs, insurance_claim_request, timeout
    )
    insurance_claim_response.guid = str(uuid.uuid4())
    loan_details = get_loan_accounts(
        session, insurance_claim_request.account_number, ""
    )
    session.commit()
    if len(loan_details) > 0:
        loan_details = loan_details[0]

    event_obj = EventOBJ(
        request=insurance_claim_response,
        application=application,
        case_number=insurance_claim_request.case_number,
        guid=insurance_claim_response.guid,
        username=current_user,
        document_type=insurance_claim_request.settlement_type,
        acquire_configs=acquire_configs,
        account_number=insurance_claim_request.account_number,
        customer_email=insurance_claim_request.customer_email,
        customer_idnumber=insurance_claim_request.customer_idnumber,
        customer_name=loan_details.customer_name or "Customer",
    )

    await send_event(event_obj)
    return insurance_claim_response


def populate_defaults(application) -> AcquireConfigs:
    statement_api = application.server_base.config.get("SataxiStatementInfo").get(
        "StatementApi"
    )
    server_details = application.server_base.config.get("SataxiStatementInfo").get(
        "ServerDetails"
    )
    url = statement_api.get("URL")
    path: str = statement_api.get("SharedPath")
    system_id: str = str(statement_api.get("SystemID"))
    system_name: str = statement_api.get("SystemName")
    period_for_quotation_validity: int = int(
        statement_api.get("PeriodforQuotationValidity")
    )
    username: str = statement_api.get("Username")
    user_id: str = str(statement_api.get("UserID"))
    server_username: str = server_details.get("Username")
    server_password: str = server_details.get("Password")
    server_name: str = server_details.get("ServerName")
    timeout: int = application.server_base.config.get("Timeout")

    return AcquireConfigs(
        url,
        path,
        system_id,
        system_name,
        period_for_quotation_validity,
        username,
        user_id,
        server_username,
        server_password,
        server_name,
        timeout,
    )


async def send_event(event_obj: EventOBJ):

    with tempfile.NamedTemporaryFile() as file_obj:
        try:
            con: SMBConnection = smb_connection_steup(event_obj.acquire_configs)
            con.retrieveFile("Storage", event_obj.request.fileName, file_obj)
            file_obj.seek(0)
            encoded_string = base64.b64encode(file_obj.read())
        except SMBTimeout as e:
            raise HTTPError(code=500, message=e.message)

    # full_path: str = (os.path.abspath("../tests/data/dummy.pdf"))
    # with open(full_path, 'wb') as fp:
    #     con.retrieveFile('Storage', event_obj.request.fileName, fp)

    event_obj.request.payload = encoded_string

    # CONTENTSTORE
    statement_generated = StatementGeneratedV1(
        event_obj.case_number,
        event_obj.username,
        event_obj.request.fileName,
        event_obj.acquire_configs.path,
        event_obj.document_type.name,
        event_obj.guid,
        event_obj.customer_idnumber,
        event_obj.customer_email,
        event_obj.account_number,
        event_obj.customer_idnumber,
        event_obj.customer_name,
    )
    event_obj.application.server_base.node.bus.send(msg_obj=statement_generated)
    event_obj.application.server_base.node.bus.commit_messaging()
    event_obj.application.server_base.node.bus.emit_prompts()
    event_obj.application.server_base.node.bus.reset_state()

    # WORKFLOW
    attach_document = AttachDocumentV1(
        int(event_obj.case_number),
        event_obj.username,
        event_obj.request.fileName.rpartition("\\")[-1],
        event_obj.guid,
    )
    event_obj.application.server_base.node.bus.send(
        msg_obj=attach_document, reply_node_id=None
    )
    event_obj.application.server_base.node.bus.commit_messaging()
    event_obj.application.server_base.node.bus.emit_prompts()
    event_obj.application.server_base.node.bus.reset_state()


def smb_connection_steup(acquire_configs: AcquireConfigs) -> SMBConnection:
    attempts = 0
    while True:
        attempts += 1
        logging.info("Connecting to SMB SERVER...")
        try:
            con = SMBConnection(
                acquire_configs.server_username,
                acquire_configs.server_password,
                "Vanguard",
                acquire_configs.server_name,
                use_ntlm_v2=True,
                is_direct_tcp=True,
            )
            url = acquire_configs.path.replace("\\\\", "").replace("\\Storage\\", "")
            con.connect(url, 445)
            logging.info("Connection to SMB SERVER Succeeded.")
            return con
        except Exception as e:
            logging.info("Failed to connect to SMB Server, retrying...")
            if attempts == 3:
                raise HTTPError(
                    504,
                    f"Failed to connect to SMB Server, retried 3 times. Reason: {e}",
                )
