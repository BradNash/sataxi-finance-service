from typing import List

from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import (
    api_response,
    api_validate,
    ParamLocation,
    api_parameter,
)
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema
from marshmallow import fields
from marshmallow_dataclass import class_schema
from tornado.web import HTTPError

from sataxi.finance.common.collect_smart import get_campaign_details
from sataxi.finance.common.collect_smart import get_ptp_details
from sataxi.finance.common.schemas.collect_smart_schema import CampaignDetailsResponse
from sataxi.finance.common.schemas.collect_smart_schema import PTPDetailsResponse


class GetPTPDetailsHandler(DBHandlerBase):
    @api_description("Get PTP details")
    @api_tag("Hive")
    @api_parameter(
        "account_number",
        "The Account Number",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(None, "200", "Accounts", PTPDetailsResponse, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, account_number: str):
        if len(account_number.strip()) == 0:
            raise HTTPError(status_code=400, reason="The account number is invalid")
        self.logger.info(f"REQUEST: Account Number - {account_number}")
        hive_session = self.sessions["HiveRepository"]
        response: List[PTPDetailsResponse] = get_ptp_details(
            hive_session, account_number
        )
        if len(response) > 0:
            self.logger.debug(f"RESPONSE: {response[0].__dict__}")
        else:
            self.logger.debug("RESPONSE: Empty result set")
        self.finish(class_schema(PTPDetailsResponse)(many=True).dump(response))


class GetCampaignDetailsHandler(DBHandlerBase):
    @api_description("Get Campaign details")
    @api_tag("Hive")
    @api_parameter(
        "account_number",
        "The Account Number",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(None, "200", "Accounts", CampaignDetailsResponse, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, account_number: str):
        if len(account_number.strip()) == 0:
            raise HTTPError(status_code=400, reason="The account number is invalid")
        self.logger.info(f"REQUEST: Account Number - {account_number}")
        hive_session = self.sessions["HiveRepository"]
        response: List[CampaignDetailsResponse] = get_campaign_details(
            hive_session, account_number
        )
        if len(response) > 0:
            self.logger.debug(f"RESPONSE: {response[0].__dict__}")
        else:
            self.logger.debug("RESPONSE: Empty result set")
        self.finish(class_schema(CampaignDetailsResponse)(many=True).dump(response))
