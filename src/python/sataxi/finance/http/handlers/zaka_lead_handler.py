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
from tornado.web import HTTPError

from sataxi.finance.common.schemas.zaka_schema import ZakaLeadDetails
from sataxi.finance.common.zaka_lead_service import get_zaka_leads_detail_by_id


class GetLeadDetails(DBHandlerBase):
    @api_description("GET the Zaka Lead Infomration")
    @api_tag("ZakaLeads")
    @api_parameter(
        "id_number",
        "ID Number of Customer",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(None, "200", "successful description", ZakaLeadDetails, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 500, "GenericFailure.", FailedResponseSchema)
    @api_validate()
    @authorized(
        "sat.fin.read", required_scopes=["sat.fin"]
    )  # TODO: need to make own operation change sat.fin.stmnt.write -> sat.fin.write ||
    # sat.signio.write/sat.signio.read
    async def get(self, id_number: str):
        session = self.sessions["HiveRepository"]
        if id_number is None or id_number == "":
            raise HTTPError(400, "BAD REQUEST 400: The Case Number cannot be empty!")
        response: ZakaLeadDetails = get_zaka_leads_detail_by_id(session, id_number)
        self.finish(class_schema(ZakaLeadDetails)().dump(response))
