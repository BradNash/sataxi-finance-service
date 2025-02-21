from dataclasses import dataclass
from datetime import datetime

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class VGDetailsLoanGomoResponse:
    account_holder: int = schema_field(
        data_key="accountHolder", required=True, allow_none=True
    )
    account_number: str = schema_field(
        data_key="accountNumber", required=True, allow_none=True
    )
    account_status: str = schema_field(
        data_key="accountStatus", required=True, allow_none=True
    )
    arrears_accrued_int: float = schema_field(
        data_key="arrearsAccruedInt", required=True, allow_none=True
    )
    bank_account_number: str = schema_field(
        data_key="bankAccountNumber", required=True, allow_none=True
    )
    bank_account_type: str = schema_field(
        data_key="bankAccountType", required=True, allow_none=True
    )
    bank_name: str = schema_field(data_key="bankName", required=True, allow_none=True)
    capital: float = schema_field(data_key="capital", required=True, allow_none=True)
    chassis_number: str = schema_field(
        data_key="chassisNumber", required=True, allow_none=True
    )
    deal_expiry_date: datetime = schema_field(
        data_key="dealExpiryDate", required=True, allow_none=True
    )
    deal_expiry_date_with_arrears: datetime = schema_field(
        data_key="dealExpiryDateWithArrears", required=True, allow_none=True
    )
    easy_pay: str = schema_field(data_key="easyPay", required=True, allow_none=True)
    engine_number: str = schema_field(
        data_key="engineNumber", required=True, allow_none=True
    )
    first_instalment_date: datetime = schema_field(
        data_key="firstInstalmentDate", required=True, allow_none=True
    )
    initial_term: int = schema_field(
        data_key="initialTerm", required=True, allow_none=True
    )
    instalment_amount: float = schema_field(
        data_key="instalmentAmount", required=True, allow_none=True
    )
    instalment_day: int = schema_field(
        data_key="instalmentDay", required=True, allow_none=True
    )
    installments_remaining: int = schema_field(
        data_key="installmentsRemaining", required=True, allow_none=True
    )
    interest_rate: str = schema_field(
        data_key="interestRate", required=True, allow_none=True
    )
    legal_fee_balance: float = schema_field(
        data_key="legalFeeBalance", required=True, allow_none=True
    )
    loan_accrued_int: float = schema_field(
        data_key="loanAccruedInt", required=True, allow_none=True
    )
    loan_start_date: datetime = schema_field(
        data_key="loanStartDate", required=True, allow_none=True
    )
    mm_code: str = schema_field(data_key="mmCode", required=True, allow_none=True)
    months_in_arrears: float = schema_field(
        data_key="monthsInArrears", required=True, allow_none=True
    )
    next_instalment_amount: float = schema_field(
        data_key="nextInstalmentAmount", required=True, allow_none=True
    )
    outstanding_balance: float = schema_field(
        data_key="outstandingBalance", required=True, allow_none=True
    )
    payment_method: str = schema_field(
        data_key="paymentMethod", required=True, allow_none=True
    )
    product: str = schema_field(data_key="product", required=True, allow_none=True)
    registration_number: str = schema_field(
        data_key="registrationNumber", required=True, allow_none=True
    )
    secondary_status: str = schema_field(
        data_key="secondaryStatus", required=True, allow_none=True
    )
    settlement_date: datetime = schema_field(
        data_key="settlementDate", required=True, allow_none=True
    )
    supplier_name: str = schema_field(
        data_key="supplierName", required=True, allow_none=True
    )
    total_due_cs: float = schema_field(
        data_key="totalDueCS", required=True, allow_none=True
    )
    total_receivable: float = schema_field(
        data_key="totalReceivable", required=True, allow_none=True
    )
    vehicle_description: str = schema_field(
        data_key="vehicleDescription", required=True, allow_none=True
    )
    year_of_manufacture: int = schema_field(
        data_key="yearOfManufacture", required=True, allow_none=True
    )
    structure_code: str = schema_field(
        data_key="structureCode", required=True, allow_none=True
    )
