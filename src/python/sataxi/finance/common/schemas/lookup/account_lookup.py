from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class AccountStatusLookupResponse:
    account_status_id: int = schema_field(data_key="accountStatusID", required=True)
    status: str = schema_field(data_key="status", required=True)


@dataclass
class AccountTypeLookupResponse:
    account_type_id: int = schema_field(data_key="accountTypeID", required=True)
    type: str = schema_field(data_key="type", required=True)
