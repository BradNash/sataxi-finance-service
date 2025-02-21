from dataclasses import dataclass

from bbdcommon.pybus.service_bus import BaseMessage
from bbdcommon.spechelpers.misc import schema_field


@dataclass
class AttachDocumentV1(BaseMessage):
    case_number: int = schema_field(data_key="caseNumber")
    current_user: str = schema_field(data_key="currentUser")
    file_name: str = schema_field(data_key="fileName")
    guid: str = schema_field(data_key="guid")
