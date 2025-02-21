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

from sataxi.finance.common.lookup.insurance_service import (
    get_all_insurance_brokers,
    get_all_insurance_companies,
    get_insurance_broker_by_name,
    get_insurance_company_by_name,
)
from sataxi.finance.db.sqlalchemy.db_InsuranceBroker import (
    DB_InsuranceBrokerSelectAll,
    DB_InsuranceBrokerSelectByBrokerName,
)
from sataxi.finance.db.sqlalchemy.db_InsuranceCompany import (
    DB_InsuranceCompanySelectAll,
    DB_InsuranceCompanySelectByCompanyName,
)


class GetAllInsuranceCompanies(DBHandlerBase):
    @api_description("Get All Insurance Companies ")
    @api_tag("Lookup")
    @api_response(
        None, "200", "Insurance Companies", DB_InsuranceCompanySelectAll, many=True
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 404, "Requested data does not exist.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_insurance_companies(self.session)
        dc = class_schema(DB_InsuranceCompanySelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetInsuranceCompanyByName(DBHandlerBase):
    @api_description("Get Insurance Company")
    @api_tag("Lookup")
    @api_parameter(
        "company_name",
        "Insurance Company Name",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(
        None,
        "200",
        "Insurance Company",
        DB_InsuranceCompanySelectByCompanyName,
        many=False,
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 404, "Requested data does not exist.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, company_name: str):
        self.logger.info(
            "INSURANCE COMPANY NAME : %s",
            json.dumps({"Insurance Company Name": company_name}),
        )
        res = get_insurance_company_by_name(self.session, company_name)
        dc = class_schema(DB_InsuranceCompanySelectByCompanyName)(many=False).dump(
            res[0]
        )
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetAllInsuranceBrokers(DBHandlerBase):
    @api_description("Get All Insurance Brokers")
    @api_tag("Lookup")
    @api_response(
        None, "200", "Insurance Brokers", DB_InsuranceBrokerSelectAll, many=True
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 404, "Requested data does not exist.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self):
        res = get_all_insurance_brokers(self.session)
        dc = class_schema(DB_InsuranceBrokerSelectAll)(many=True).dump(res)
        self.logger.debug(json.dumps(dc))
        self.finish(dc)


class GetInsuranceBrokerByName(DBHandlerBase):
    @api_description("Get Insurance Broker")
    @api_tag("Lookup")
    @api_parameter(
        "broker_name",
        "Insurance Broker Name",
        fields.String(required=True),
        location=ParamLocation.Query,
    )
    @api_response(
        None,
        "200",
        "Insurance Broker",
        DB_InsuranceBrokerSelectByBrokerName,
        many=False,
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 404, "Requested data does not exist.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("sat.fin.read", required_scopes=["sat.fin"])
    def get(self, broker_name: str):
        res = get_insurance_broker_by_name(self.session, broker_name)
        dc = class_schema(DB_InsuranceBrokerSelectByBrokerName)(many=False).dump(res[0])
        self.logger.debug(json.dumps(dc))
        self.finish(dc)
