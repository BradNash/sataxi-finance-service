import json

from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import (
    ParamLocation,
    api_parameter,
    api_response,
    api_validate,
)
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema
from marshmallow import fields
from marshmallow_dataclass import class_schema

from sataxi.finance.common.lookup.language_service import (
    get_all_languages,
    get_language_by_description,
)
from sataxi.finance.db.sqlalchemy.db_Language import (
    DB_LanguageSelectAll,
    DB_LanguageSelectByDescription,
)


class GetAllLanguages(DBHandlerBase):
    @api_description("Get All Languages")
    @api_tag("Lookup")
    @api_response(None, "200", "Languages", DB_LanguageSelectAll, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 404, "Requested data does not exist.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_languages(self.session)
        dc = class_schema(DB_LanguageSelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetLanguageByDescription(DBHandlerBase):
    @api_description("Get Language by Language")
    @api_tag("Lookup")
    @api_parameter(
        "description",
        "Description",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(None, "200", "Language", DB_LanguageSelectByDescription, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 404, "Requested data does not exist.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, description: str):
        res = get_language_by_description(self.session, description)
        dc = class_schema(DB_LanguageSelectByDescription)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)
