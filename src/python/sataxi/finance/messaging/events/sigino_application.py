from dataclasses import dataclass
from typing import Optional

from bbdcommon.pybus.service_bus import BaseMessage
from bbdcommon.spechelpers.misc import schema_field


@dataclass
class SignioApplicationGeneratedV1(BaseMessage):
    content_type: int = schema_field(data_key="contentType")
    source_type: int = schema_field(data_key="sourceType")
    source_id: str = schema_field(data_key="sourceID")
    user: str = schema_field(data_key="user")
    user_specified_key: str = schema_field(data_key="userSpecifiedKey")
    file_name: str = schema_field(data_key="fileName")
    mime_type: str = schema_field(data_key="mimeType")
    encryption_password: Optional[str] = schema_field(data_key="encryptionPassword")
    signio_application_data: dict = schema_field(data_key="siginoApplicationData")
