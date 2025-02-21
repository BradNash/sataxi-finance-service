from dataclasses import dataclass
from datetime import datetime

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class TransactionHistoryResponse:
    account_number: str = schema_field(data_key="accountNumber")
    post_date: datetime = schema_field(data_key="postDate")
    effective_date: datetime = schema_field(data_key="effectiveDate")
    transaction_type: str = schema_field(data_key="transactionType")
    narrative: str = schema_field(data_key="narrative")
    transaction_amount: float = schema_field(data_key="transactionAmount")
    customer_account_type: str = schema_field(data_key="customerAccountType")
    capital_balance: float = schema_field(data_key="capitalBalance")
    arrears_balance: float = schema_field(data_key="arrearsBalance")
    total_balance: float = schema_field(data_key="totalBalance")
    structure_name: str = schema_field(data_key="structureName")
