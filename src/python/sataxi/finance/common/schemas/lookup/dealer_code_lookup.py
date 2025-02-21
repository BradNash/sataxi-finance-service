from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class DealerCodeLookupResponse:
    dealer_code_id: int = schema_field(data_key="dealerCodeID", required=True)
    d_code: str = schema_field(data_key="dCode", required=True)
