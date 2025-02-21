from typing import List

from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import (
    api_response,
    api_parameter,
    api_validate,
    class_schema,
    ParamLocation,
)
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema

# marshmallow
from marshmallow import fields

# tornado
from tornado.web import HTTPError

from sataxi.finance.common.schemas.transaction_history_schema import (
    TransactionHistoryResponse,
)
from sataxi.finance.common.transaction_history_service import get_transaction_history


class GetTransactionHistory(DBHandlerBase):
    @api_description("Get Transaction history")
    @api_tag("Hive")
    @api_parameter(
        "account_number",
        "The Account Number",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(None, "200", "Account Details", TransactionHistoryResponse, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, account_number: str):
        if len(account_number.strip()) == 0:
            raise HTTPError(
                status_code=400, log_message="The account number is invalid"
            )
        self.logger.info(f"REQUEST: Account Number - {account_number}")
        hive_session = self.sessions["HiveRepository"]
        response: List[TransactionHistoryResponse] = get_transaction_history(
            hive_session, account_number
        )
        if len(response) > 0:
            self.logger.debug(f"RESPONSE: {response[0].__dict__}")
        else:
            self.logger.debug("RESPONSE: Empty result set")
        self.finish(class_schema(TransactionHistoryResponse)(many=True).dump(response))
