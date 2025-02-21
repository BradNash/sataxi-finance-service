from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class DocumentType(Enum):
    EARLY_SETTLEMENT = "Early Settlement"
    DEAL_TAKEOVER_GENERIC = "Deal Takeover Generic"
    DEAL_TAKEOVER_DECEASED = "Deal Takeover Deceased"
    INSURANCE_CLAIM = "Insurance Settlement"
    STATEMENT = "Statement"


@dataclass
class Base:
    timeout: int = schema_field(data_key="timeout", required=False, allow_none=True)


# NOTICE SETTLEMENT REQUEST
@dataclass
class NoticeSettlementRequest(Base):
    account_number: str = schema_field(data_key="accountNumber", required=True)
    notice_date: datetime = schema_field(
        data_key="noticeDate", required=True, default=datetime.now()
    )


@dataclass
class NoticeSettlementResponse:
    message: str = schema_field(data_key="message")
    notice_start_date: str = schema_field(data_key="noticeStartDate")
    notice_end_date: str = schema_field(data_key="noticeEndDate")
    remaining_date: str = schema_field(data_key="remainingDays")


@dataclass
class AcquireNoticeSettlementRequest:
    # Not snake case for acquire api, Find a way to use schema_field maybe?
    accountNumber: str = schema_field(data_key="accountNumber", required=True)
    noticeDate: str = schema_field(data_key="noticeDate", required=True)
    systemName: str = schema_field(data_key="systemName", required=True)
    systemID: str = schema_field(data_key="systemID", required=True)
    userID: str = schema_field(data_key="userID", required=True)


@dataclass
class InsuranceClaimRequest(Base):
    account_number: str = schema_field(data_key="accountNumber", required=True)
    settlement_type: DocumentType = schema_field(
        data_key="settlementType", required=True
    )
    continue_car_track: bool = schema_field(data_key="continueCartrack", required=True)
    case_number: str = schema_field(data_key="caseNumber", required=True)
    customer_email: str = schema_field(data_key="customerEmail")
    customer_idnumber: str = schema_field(data_key="customerID")
    legal_fees_payable: str = schema_field(data_key="legalFeesPayble", required=True)
    legal_notes: str = schema_field(data_key="legalNotes", required=True)
    is_ins_settlement: bool = schema_field(data_key="IsInsSettlement", required=True)
    date_of_loss: str = schema_field(data_key="dateOfLoss", required=True)


@dataclass
class InsuranceClaimResponse:
    path: str = schema_field(data_key="path")
    fileName: str = schema_field(data_key="fileName")
    message: str = schema_field(data_key="message")
    payload: bytes = schema_field(data_key="payload", allow_none=True, default="")
    guid: str = schema_field(data_key="guid", allow_none=True, default="")


@dataclass
class AcquireInsuranceClaimRequest:
    deal_number: str = schema_field(data_key="dealNumber", required=True)
    settlement_type: str = schema_field(data_key="settlementType", required=True)
    continue_car_track: bool = schema_field(data_key="continueCartrack", required=True)
    period_for_quotation_validity: int = schema_field(
        data_key="periodforQuotationValidity", required=True
    )
    system_id: str = schema_field(data_key="systemID", required=True)
    user_id: str = schema_field(data_key="userID", required=True)
    path: str = schema_field(data_key="path", required=True)
    legal_fees_payable: str = schema_field(data_key="legalFeesPayble", required=True)
    legal_notes: str = schema_field(data_key="legalNotes", required=True)
    is_ins_settlement: bool = schema_field(data_key="IsINSSettlement", required=True)
    user_name: str = schema_field(data_key="userName", required=True)
    date_of_loss: str = schema_field(data_key="dateOfLoss", required=True)


# SETTLEMENT REQUEST
@dataclass
class SettlementRequest(Base):
    deal_number: str = schema_field(data_key="dealNumber", required=True)
    settlement_type: DocumentType = schema_field(
        data_key="settlementType", required=True
    )
    continue_car_track: bool = schema_field(data_key="continueCartrack", required=True)
    case_number: str = schema_field(data_key="caseNumber", required=True)
    customer_email: str = schema_field(data_key="customerEmail")
    customer_idnumber: str = schema_field(data_key="customerID")


@dataclass
class AcquireSettlementRequest:
    # Not snake case for acquire api, Find a way to use schema_field maybe?
    dealNumber: str = schema_field(data_key="dealNumber", required=True)
    settlementType: str = schema_field(data_key="settlementType", required=True)
    continueCartrack: bool = schema_field(data_key="continueCartrack", required=True)
    userID: str = schema_field(data_key="userID", required=True)
    path: str = schema_field(data_key="path", required=True)
    systemID: str = schema_field(data_key="systemID", required=True)
    periodforQuotationValidity: int = schema_field(
        data_key="periodforQuotationValidity", required=True
    )


@dataclass
class SettlementResponse:
    path: str = schema_field(data_key="path")
    fileName: str = schema_field(data_key="fileName")
    message: str = schema_field(data_key="message")
    payload: bytes = schema_field(data_key="payload", allow_none=True, default="")
    guid: str = schema_field(data_key="guid", allow_none=True, default="")


# STATEMENT REQUEST
@dataclass
class StatementRequest(Base):
    account_number: str = schema_field(data_key="accountNumber", required=True)
    start_date: datetime = schema_field(data_key="startDate", required=True)
    case_number: str = schema_field(data_key="caseNumber", required=True)
    customer_email: str = schema_field(data_key="customerEmail")
    customer_idnumber: str = schema_field(data_key="customerID")


@dataclass
class AcquireStatementRequest:
    # Not snake case for acquire api, Find a way to use schema_field maybe?
    accountNumber: str = schema_field(data_key="accountNumber", required=True)
    startDate: str = schema_field(data_key="startDate", required=True)
    userID: str = schema_field(data_key="userID", required=True)
    filePath: str = schema_field(data_key="filePath", required=True)
    systemID: str = schema_field(data_key="systemID", required=True)
    systemName: str = schema_field(data_key="systemName", required=True)


@dataclass
class StatementResponse:
    path: str = schema_field(data_key="path")
    fileName: str = schema_field(data_key="fileName")
    message: str = schema_field(data_key="message")
    payload: bytes = schema_field(data_key="payload", allow_none=True, default="")
    guid: str = schema_field(data_key="guid", allow_none=True, default="")
