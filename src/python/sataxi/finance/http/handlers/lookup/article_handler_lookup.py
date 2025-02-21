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

from sataxi.finance.db.sqlalchemy.db_ArticleType import (
    DB_ArticleTypeSelectAll,
    DB_ArticleTypeSelectByType,
)
from ....common.lookup.article_service import (
    get_all_article_types,
    get_article_type_by_type,
)

"""
ARTICLE TYPE
"""


class GetAllArticleTypes(DBHandlerBase):
    @api_description("Get All Article Types")
    @api_tag("Lookup")
    @api_response(None, "200", "Article Types", DB_ArticleTypeSelectAll, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_article_types(self.session)
        dc = class_schema(DB_ArticleTypeSelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetArticleTypeByType(DBHandlerBase):
    @api_description("Get Article Type")
    @api_tag("Lookup")
    @api_parameter(
        "article_type",
        "Article Type",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(None, "200", "Article Type", DB_ArticleTypeSelectByType, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, article_type: str):
        self.logger.info(
            "ARTICLE TYPE : %s", json.dumps({"Article Type": article_type})
        )
        res = get_article_type_by_type(self.session, article_type)
        dc = class_schema(DB_ArticleTypeSelectByType)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)
