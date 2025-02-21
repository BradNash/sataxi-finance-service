from dataclasses import dataclass
from datetime import date, datetime

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class LoanAccountLookupRequest:
    account_number: str = schema_field(data_key="accountNumber", required=True)
    id_number: str = schema_field(data_key="idNo", required=True)


@dataclass
class LoanAccountLookupResponse:
    account_number: str = schema_field(data_key="accountNumber")
    id_no: str = schema_field(data_key="idNo")
    customer_name: str = schema_field(data_key="customerName")
    mobile: str = schema_field(data_key="mobile")
    taxi_association: str = schema_field(data_key="taxiAssociation")
    residential_address: str = schema_field(data_key="residentialAddress",)
    postal_address: str = schema_field(data_key="postalAddress")
    next_instalment_date: str = schema_field(data_key="nextInstalmentDate")
    instalment_day: str = schema_field(data_key="instalmentDay")
    payment_type: str = schema_field(data_key="paymentType")
    loan_start_date: datetime = schema_field(data_key="loanStartDate")
    bank_account_number: str = schema_field(data_key="bankAccountNumber")
    bank_account_type: str = schema_field(data_key="bankAccountType")
    bank_name: str = schema_field(data_key="bankName")
    account_status: str = schema_field(data_key="accountStatus")
    total_due_cs: float = schema_field(data_key="totalDueCS")
    email_address: str = schema_field(data_key="emailAddress")


@dataclass
class LoanDetailsLookupResponse:
    account_number: str = schema_field(data_key="accountNumber")
    instalment_day: int = schema_field(data_key="instalmentDay")
    account_status: str = schema_field(data_key="accountStatus")
    loan_start_date: datetime = schema_field(data_key="loanStartDate")
    payment_method: str = schema_field(data_key="paymentMethod")
    account_holder: str = schema_field(data_key="accountHolder")
    bank_account_number: str = schema_field(data_key="bankAccountNumber")
    bank_account_type: str = schema_field(data_key="bankAccountType")
    bank_name: str = schema_field(data_key="bankName")
    vehicle_description: str = schema_field(data_key="vehicleDescription")
    total_due_cs: float = schema_field(data_key="totalDueCS")
    device_health: str = schema_field(data_key="deviceHealth")
    car_track_signal_date: datetime = schema_field(data_key="carTrackSignalDate")
    capital: float = schema_field(data_key="capital")
    outstanding_balance: float = schema_field(data_key="outstandingBalance")
    installment_amount: float = schema_field(data_key="installmentAmount")
    next_installment_amount: float = schema_field(data_key="nextInstallmentAmount")
    next_instalment_date: date = schema_field(data_key="nextInstalmentDate")
    legal_fee_balance: float = schema_field(data_key="legalFeeBalance")
    deal_expiry_date: datetime = schema_field(data_key="dealExpiryDate")
    loan_accrued_int: float = schema_field(data_key="loanAccruedInt")
    total_receivable: float = schema_field(data_key="totalReceivable")
    interest_rate: str = schema_field(data_key="interestRate")
    initial_term: int = schema_field(data_key="initialTerm")
    instalments_remaining: int = schema_field(data_key="instalmentsRemaining")
    months_in_arrears: float = schema_field(data_key="monthsInArrears")
    deal_expiry_date_with_arrear: datetime = schema_field(
        data_key="dealExpiryDateWithArrears"
    )
    settlement_date: datetime = schema_field(data_key="settlementDate")
    chassis_number: str = schema_field(data_key="chassisNumber")
    engine_number: str = schema_field(data_key="engineNumber")
    year_of_manufacture: int = schema_field(data_key="yearOfManufacture")
    registration_number: int = schema_field(data_key="registrationNumber")
    first_instalment_date: date = schema_field(data_key="firstInstalmentDate")
    product: str = schema_field(data_key="product")
    easy_pay: str = schema_field(data_key="easyPay")
    source: str = schema_field(data_key="source")
    field_agent: str = schema_field(data_key="fieldAgent")
    field_agent_instruction: str = schema_field(data_key="fieldAgentInstructions")
    company_name: str = schema_field(data_key="companyName")
    ncr_reg_no: str = schema_field(data_key="ncrRegNo")
    previous_company_name: str = schema_field(data_key="previousCompanyName")
