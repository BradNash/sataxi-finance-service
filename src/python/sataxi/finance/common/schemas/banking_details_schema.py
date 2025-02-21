from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class BankingDetailsLookupResponse:
    bank_name: str = schema_field(data_key="bankName")
    branch_type: str = schema_field(data_key="branchType")
    account_no: str = schema_field(data_key="accountNo")
    expr_1: str = schema_field(data_key="expr1")
    bank_reference: str = schema_field(data_key="bankReference")
