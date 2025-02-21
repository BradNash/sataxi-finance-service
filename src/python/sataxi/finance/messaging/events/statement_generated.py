from dataclasses import dataclass

from bbdcommon.pybus.service_bus import BaseMessage
from bbdcommon.spechelpers.misc import schema_field


@dataclass
class StatementGeneratedV1(BaseMessage):
    case_number: str = schema_field(data_key="caseNumber")
    username: str = schema_field(data_key="username")
    file_name: str = schema_field(data_key="fileName")
    shared_path: str = schema_field(data_key="sharedPath")
    document_type: str = schema_field(data_key="document_type")
    guid: str = schema_field(data_key="guid")
    encryption_password: str = schema_field(data_key="encryption_password")
    customer_email: str = schema_field(data_key="customerEmail")
    account_number: str = schema_field(data_key="accountNumber")
    id_number: str = schema_field(data_key="idNumber")
    customer_name: str = schema_field(data_key="customerName")
