from dataclasses import dataclass
from datetime import datetime

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class InstalmentBreakdownLookUpResponse:
    account_number: str = schema_field(data_key="accountNumber")
    description: str = schema_field(data_key="description")
    value_date: datetime = schema_field(data_key="valueDate")
    instalment_amount: float = schema_field(data_key="instalmentAmount")
