from dataclasses import dataclass
from datetime import datetime

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class VGDetailsLoanInstallmentGomoResponse:
    account_number: str = schema_field(data_key="accountNumber", required=True)
    description: str = schema_field(data_key="description", required=True)
    value_date: datetime = schema_field(data_key="valueDate", required=True)
    installment_amount: float = schema_field(data_key="instalmentAmount", required=True)
