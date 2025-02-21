from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import (
    api_response,
    api_validate,
    api_parameter,
    ParamLocation,
)
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema
from marshmallow import fields
from marshmallow_dataclass import class_schema

from sataxi.finance.common.documents_service import get_available_documents_for_client
from sataxi.finance.common.schemas.documents_schema import DocumentsResponse, Company


class DocumentsHandler(DBHandlerBase):
    @api_description("GET Available Documents for client")
    @api_tag("Documents")
    @api_parameter(
        "account_number",
        "Account Number of Client",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(None, "200", "successful description", DocumentsResponse, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 500, "GenericFailure.", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    async def get(self, account_number: str):
        session = self.sessions["HiveRepository"]
        response = get_available_documents_for_client(
            session, account_number, Company.SAT
        )
        self.finish(class_schema(DocumentsResponse)(many=False).dump(response))
