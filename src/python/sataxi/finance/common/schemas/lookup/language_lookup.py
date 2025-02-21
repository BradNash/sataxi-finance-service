from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class LanguageLookupResponse:
    language_id: int = schema_field(data_key="languageID", required=True)
    description: str = schema_field(data_key="description", required=True)
