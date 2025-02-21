from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class InsuranceCompanyLookupResponse:
    company_id: int = schema_field(data_key="companyID", required=True)
    company_name: str = schema_field(data_key="companyName", required=True)


@dataclass
class InsuranceBrokerLookupResponse:
    broker_id: int = schema_field(data_key="brokerID", required=True)
    broker_name: str = schema_field(data_key="brokerName", required=True)
