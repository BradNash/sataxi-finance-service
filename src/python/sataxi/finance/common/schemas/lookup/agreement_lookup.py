from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class AgreementLookupResponse:
    agreement_id: int = schema_field(data_key="agreementID", required=True)
    description: str = schema_field(data_key="description", required=True)
