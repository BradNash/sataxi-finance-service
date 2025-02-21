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

from sataxi.finance.common.banking_details_lookup import get_banking_details
from sataxi.finance.common.lookup.bank_service import get_all_banks, get_bank_by_name
from sataxi.finance.common.schemas.banking_details_schema import (
    BankingDetailsLookupResponse,
)
from sataxi.finance.db.sqlalchemy.db_Bank import (
    DB_BankSelectAll,
    DB_BankSelectByBankName,
)


class BankingDetailsLookup(DBHandlerBase):
    @api_description("Get Sataxi Banking Details")
    @api_tag("Hive")
    @api_parameter(
        "bank_ref",
        "Bank Ref",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(
        None, "200", "Banking Details", BankingDetailsLookupResponse, many=True
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, bank_ref: str):
        session = self.sessions["HiveRepository"]
        self.logger.info(f"BANK REFERENCE : Bank Reference: {bank_ref}")
        res = get_banking_details(session, bank_ref)
        self.finish(class_schema(BankingDetailsLookupResponse)(many=True).dump(res))


class GetAllBanks(DBHandlerBase):
    @api_description("Get All Banks")
    @api_tag("Lookup")
    @api_response(None, "200", "Banks", DB_BankSelectAll, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_banks(self.session)
        dc = class_schema(DB_BankSelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetBankByName(DBHandlerBase):
    @api_description("Get Bank by Bank Name")
    @api_tag("Lookup")
    @api_parameter(
        "bank_name", "Bank", fields.String(required=True), location=ParamLocation.Query
    )
    @api_response(None, "200", "Bank Name", DB_BankSelectByBankName, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, bank_name: str):
        self.logger.info("BANK : %s", json.dumps({"Bank Name": bank_name}))
        res = get_bank_by_name(self.session, bank_name)
        dc = class_schema(DB_BankSelectByBankName)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)
