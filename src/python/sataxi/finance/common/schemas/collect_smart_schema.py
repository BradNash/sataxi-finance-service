from dataclasses import dataclass
from datetime import datetime

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class CollectSmartClientDetailsResponse:
    account_number: str = schema_field(data_key="accountNumber")
    account_holder: str = schema_field(data_key="accountHolder")
    account_status: str = schema_field(data_key="accountStatus")
    vehicle_description: str = schema_field(data_key="vehicleDescription")
    total_due_cs: int = schema_field(data_key="totalDueCs")
    device_health: str = schema_field(data_key="deviceHealth")
    cartrack_signal_date: datetime = schema_field(data_key="cartrackSignalDate")
    capital: int = schema_field(data_key="capital")
    outstanding_balance: int = schema_field(data_key="outstandingBalance")
    installment_amount: int = schema_field(data_key="installmentAmount")
    next_installment_amount: int = schema_field(data_key="nextInstallmentAmount")
    legal_fee_balance: int = schema_field(data_key="legalFeeBalance")
    deal_expiry_date: datetime = schema_field(data_key="dealExpiryDate")
    loan_accrued_int: int = schema_field(data_key="loanAccruedInt")
    total_receivable: int = schema_field(data_key="totalReceivable")
    interestrate: str = schema_field(data_key="interestrate")
    initialterm: int = schema_field(data_key="initialterm")
    instalments_remaining: int = schema_field(data_key="instalmentsRemaining")
    months_in_arrears: int = schema_field(data_key="monthsInArrears")
    deal_expiry_date_with_arrears: datetime = schema_field(
        data_key="dealExpiryDateWithArrears"
    )
    settlementdate: datetime = schema_field(data_key="settlementdate")
    chassisnumber: str = schema_field(data_key="chassisnumber")
    enginenumber: str = schema_field(data_key="enginenumber")
    yearofmanufacture: int = schema_field(data_key="yearofmanufacture")
    registrationnumber: int = schema_field(data_key="registrationnumber")
    first_instalment_date: datetime = schema_field(data_key="firstInstalmentDate")
    product: str = schema_field(data_key="product")
    easy_pay: str = schema_field(data_key="easyPay")
    agent: str = schema_field(data_key="agent")
    supervisor: str = schema_field(data_key="supervisor")
    payment_mtd: int = schema_field(data_key="paymentMtd")
    arrears_accrued_int: int = schema_field(data_key="arrearsAccruedInt")
    short_over: int = schema_field(data_key="shortOver")
    secondary_status: str = schema_field(data_key="secondaryStatus")
    last_payment_date: datetime = schema_field(data_key="lastPaymentDate")
    last_payment_amount: int = schema_field(data_key="lastPaymentAmount")
    pending_activity: int = schema_field(data_key="pendingActivity")
    legal_administrator: str = schema_field(data_key="legalAdministrator")
    attorney: str = schema_field(data_key="attorney")
    handover_date: datetime = schema_field(data_key="handoverDate")
    arrears_amountat_ho: int = schema_field(data_key="arrearsAmountatHo")
    ls_case_number: str = schema_field(data_key="lsCaseNumber")
    summons_issue_date: datetime = schema_field(data_key="summonsIssueDate")
    summons_served_date: datetime = schema_field(data_key="summonsServedDate")
    dateof_judgement: datetime = schema_field(data_key="dateofJudgement")
    warrant_issued_date: datetime = schema_field(data_key="warrantIssuedDate")
    source: str = schema_field(data_key="source")
    field_agent: str = schema_field(data_key="fieldAgent")
    field_agent_instruction: str = schema_field(data_key="fieldAgentInstruction")


@dataclass
class PTPDetailsResponse:
    account_number: str = schema_field(data_key="accountNumber")
    agent_id: int = schema_field(data_key="agentId")
    campaign_date: datetime = schema_field(data_key="campaignDate")
    campaign_id: int = schema_field(data_key="campaignId")
    campaign_name: str = schema_field(data_key="campaignName")
    client_id: int = schema_field(data_key="clientId")
    current_payment: int = schema_field(data_key="currentPayment")
    frequency: str = schema_field(data_key="frequency")
    name: str = schema_field(data_key="name")
    ptp_amount: int = schema_field(data_key="ptpAmount")
    ptp_created_date: datetime = schema_field(data_key="ptpCreatedDate")
    ptp_date: datetime = schema_field(data_key="ptpDate")
    ptpid: int = schema_field(data_key="ptpid")
    ptp_status: str = schema_field(data_key="ptpStatus")
    ptp_type: str = schema_field(data_key="ptpType")
    user_name: str = schema_field(data_key="userName")


@dataclass
class CampaignDetailsResponse:
    note_text: str = schema_field(data_key="noteText")
    note_category: str = schema_field(data_key="noteCategory")
    username: str = schema_field(data_key="userName")
    note_system: str = schema_field(data_key="noteSystem")
    created_date: datetime = schema_field(data_key="createdDate")
