from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class BankLookupResponse:
    bank_id: int = schema_field(data_key="bankID", required=True)
    bank_name: str = schema_field(data_key="bankName", required=True)
