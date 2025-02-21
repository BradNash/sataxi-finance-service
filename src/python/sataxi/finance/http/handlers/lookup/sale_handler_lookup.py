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

from sataxi.finance.common.lookup.sale_service import (
    get_all_type_of_sales,
    get_type_of_sale_by_type,
)
from sataxi.finance.db.sqlalchemy.db_TypeOfSale import (
    DB_TypeOfSaleSelectAll,
    DB_TypeOfSaleSelectByType,
)


class GetAllTypeOfSales(DBHandlerBase):
    @api_description("Get All Type Of Sales")
    @api_tag("Lookup")
    @api_response(None, "200", "Type Of Sales", DB_TypeOfSaleSelectAll, many=True)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_type_of_sales(self.session)
        dc = class_schema(DB_TypeOfSaleSelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetTypeOfSaleByType(DBHandlerBase):
    @api_description("Get TypeOfSale by Type")
    @api_tag("Lookup")
    @api_parameter(
        "type", "Type", fields.String(required=True), location=ParamLocation.Query
    )
    @api_response(None, "200", "TypeOfSale", DB_TypeOfSaleSelectByType, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, type: str):
        res = get_type_of_sale_by_type(self.session, type)
        dc = class_schema(DB_TypeOfSaleSelectByType)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)
