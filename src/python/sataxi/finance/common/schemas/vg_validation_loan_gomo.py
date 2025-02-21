from dataclasses import dataclass
from datetime import datetime

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class VGValidationLoanGomoResponse:
    account_number: str = schema_field(
        data_key="accountNumber", required=True, allow_none=True
    )
    id_no: str = schema_field(data_key="idNo", required=True, allow_none=True)
    customer_name: str = schema_field(
        data_key="customerName", required=True, allow_none=True
    )
    mobile: str = schema_field(data_key="mobile", required=True, allow_none=True)
    physical_address: str = schema_field(
        data_key="physicalAddress", required=True, allow_none=True
    )
    postal_address: str = schema_field(
        data_key="postalAddress", required=True, allow_none=True
    )
    next_instalment_date: datetime = schema_field(
        data_key="nextInstalmentDate", required=True, allow_none=True
    )
    instalment_day: int = schema_field(
        data_key="instalmentDay", required=True, allow_none=True
    )
    payment_typ: str = schema_field(
        data_key="paymentType", required=True, allow_none=True
    )
    loan_start_date: datetime = schema_field(
        data_key="loanStartDate", required=True, allow_none=True
    )
    bank_account_number: str = schema_field(
        data_key="bankAccountNumber", required=True, allow_none=True
    )
    bank_account_type: str = schema_field(
        data_key="bankAccountType", required=True, allow_none=True
    )
    bank_name: str = schema_field(data_key="bankName", required=True, allow_none=True)
    account_status: str = schema_field(
        data_key="accountStatus", required=True, allow_none=True
    )
    email_address: str = schema_field(
        data_key="emailAddress", required=True, allow_none=True
    )
    total_due_cs: float = schema_field(
        data_key="totalDueCS", required=True, allow_none=True
    )
    structure_code: str = schema_field(
        data_key="structureCode", required=True, allow_none=True
    )
