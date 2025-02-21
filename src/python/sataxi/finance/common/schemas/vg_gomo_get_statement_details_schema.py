from dataclasses import dataclass
from datetime import datetime

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class VGGomoGetStatementDetailsResponse:
    row_no: int = schema_field(data_key="rowNo", required=True, allow_none=True)
    account_number: str = schema_field(
        data_key="accountNumber", required=True, allow_none=True
    )
    post_date: datetime = schema_field(
        data_key="postDate", required=True, allow_none=True
    )
    effective_date: datetime = schema_field(
        data_key="effectiveDate", required=True, allow_none=True
    )
    transaction_type: str = schema_field(
        data_key="transactionType", required=True, allow_none=True
    )
    narrative: str = schema_field(data_key="narrative", required=True, allow_none=True)
    debit_amount: float = schema_field(
        data_key="debitAmount", required=True, allow_none=True
    )
    credit_amount: float = schema_field(
        data_key="creditAmount", required=True, allow_none=True
    )
    customer_account_type: str = schema_field(
        data_key="customerAccountType", required=True, allow_none=True
    )
    simplified_description: str = schema_field(
        data_key="simplifiedDescription", required=True, allow_none=True
    )
    arrears_balance: float = schema_field(
        data_key="arrearsBalance", required=True, allow_none=True
    )
    capital_balance: float = schema_field(
        data_key="capitalBalance", required=True, allow_none=True
    )
    total_balance: float = schema_field(
        data_key="totalBalance", required=True, allow_none=True
    )
    id_number: str = schema_field(data_key="idNumber", required=True, allow_none=True)
