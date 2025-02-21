from dataclasses import dataclass
from typing import List

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class AcquireConfigs:
    url: str = schema_field(data_key="url")
    path: str = schema_field(data_key="path")
    system_id: str = schema_field(data_key="system_id")
    system_name: str = schema_field(data_key="system_name")
    period_for_quotation_validity: int = schema_field(
        data_key="period_for_quotation_validity"
    )
    username: str = schema_field(data_key="username")
    user_id: str = schema_field(data_key="user_id")
    server_username: str = schema_field(data_key="server_username")
    server_password: str = schema_field(data_key="server_password")
    server_name: str = schema_field(data_key="server_name")
    timeout: int = schema_field(data_key="timeout")
    date_format: str = schema_field(data_key="date_format", default="%Y-%m-%d")


@dataclass
class SignioConfigs:
    url: str = schema_field(data_key="url")
    auth_token: str = schema_field(data_key="auth_token")
    authorisation: str = schema_field(data_key="authorisation")
    dealer_codes: List[dict] = schema_field(data_key="dealer_codes")
