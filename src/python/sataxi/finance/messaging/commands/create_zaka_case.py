from datetime import datetime
from typing import Dict, List, Optional

from bbdcommon.pybus.service_bus import BaseMessage
from bbdcommon.spechelpers.misc import schema_field
from marshmallow.validate import Length, Range
from marshmallow_dataclass import dataclass


@dataclass
class ProcessData:
    sys_id: int = schema_field(data_key="sysID", required=True)
    data: Dict[str, str] = schema_field(required=True)


@dataclass
class ProcessDataExt:
    sys_id: int = schema_field(data_key="sysID", required=True)
    data: str = schema_field(required=True)


@dataclass
class CaseReferenceSecondry:
    reference_type: int = schema_field(data_key="referenceType")
    reference: str = schema_field(data_key="reference", validate=Length(min=0, max=64))


@dataclass
class ZakaCreateCaseV1(BaseMessage):
    process_type_sysid: int = schema_field(
        data_key="processTypeSysID", example=776041824
    )
    reference_type: int = schema_field(data_key="referenceType", missing=None)
    reference: str = schema_field(data_key="reference", missing="")
    reference_year: Optional[int] = schema_field(
        data_key="referenceYear",
        allow_none=True,
        missing=None,
        validate=Range(
            min=1900, max=int(datetime.now().year), error="referenceYear is invalid."
        ),
        example=datetime.now().year,
    )
    area_code: str = schema_field(
        data_key="areaCode", validate=Length(min=0, max=10), missing=""
    )
    status: str = schema_field(
        data_key="status", validate=Length(min=0, max=200), missing=""
    )
    channel: str = schema_field(
        data_key="channel", validate=Length(min=0, max=15), missing=""
    )
    title: str = schema_field(
        data_key="title", validate=Length(min=0, max=200), missing=""
    )
    process_data: List[ProcessData] = schema_field(
        data_key="processData", example=[], missing=[]
    )
    process_data_extensions: List[ProcessDataExt] = schema_field(
        data_key="processDataExtensions", example=[], missing=[]
    )
    additional_references: List[CaseReferenceSecondry] = schema_field(
        data_key="additionalReferences", example=[], missing=[]
    )
    id_number: str = schema_field(data_key="idNumber")
    engine_number: str = schema_field(data_key="engineNumber")
    campaign: str = schema_field(data_key="campaign")
    user: str = schema_field(data_key="user", default=None)
