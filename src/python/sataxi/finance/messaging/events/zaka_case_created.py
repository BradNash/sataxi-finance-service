from datetime import datetime
from typing import Optional

from bbdcommon.pybus.service_bus import BaseMessage
from bbdcommon.spechelpers.misc import schema_field
from marshmallow.validate import Length
from marshmallow_dataclass import dataclass


@dataclass
class ZakaCaseCreatedV1(BaseMessage):
    case_no: int = schema_field(data_key="caseNo")
    id_number: str = schema_field(data_key="idNumber")
    engine_number: str = schema_field(data_key="engineNumber")
    campaign: str = schema_field(data_key="campaign")
    reference_type_name: str = schema_field(data_key="referenceTypeName", missing="")
    date_created: datetime = schema_field(data_key="dateCreated")
    created_by: str = schema_field(
        data_key="createdBy", validate=Length(min=0, max=100)
    )
    parent_case_no: Optional[int] = schema_field(
        data_key="parentCaseNo", allow_none=True
    )
    error: str = schema_field(data_key="error", default=None)
