import logging
import os
import sys

from bbdcommon.pybus.py_node import PyNode
from bbdcommon.tornadohelpers.base.tornado_app_service_base import AppServiceBase

from sataxi.finance.http.handlers.acquire_handler import (
    AcquireStatement,
    AcquireSettlement,
    AcquireNoticeSettlement,
    AcquireInsuranceClaim,
)
from sataxi.finance.http.handlers.banking_details_lookup_handler import (
    GetAllBanks,
    GetBankByName,
    BankingDetailsLookup,
)
from sataxi.finance.http.handlers.client_type_handler_lookup import (
    GetAllClientTypes,
    GetClientTypeByType,
)
from sataxi.finance.http.handlers.collect_smart_handler import GetCampaignDetailsHandler
from sataxi.finance.http.handlers.collect_smart_handler import GetPTPDetailsHandler
from sataxi.finance.http.handlers.documents_handler import DocumentsHandler
from sataxi.finance.http.handlers.gomo.get_statement_details_handler import (
    VGGomoGetStatementDetailsHandler,
)
from sataxi.finance.http.handlers.gomo.details_loan_gomo_handler import (
    VGDetailsLoanGomoHandler,
)
from sataxi.finance.http.handlers.gomo.details_loaninstallment_gomo_handler import (
    VGDetailsLoanInstallmentGomoHandler,
)
from sataxi.finance.http.handlers.gomo.documents_handler import (
    DocumentsHandler as GDocumentsHandler,
)
from sataxi.finance.http.handlers.gomo.validation_loan_gomo_handler import (
    VGValidationLoanGomoHandler,
)
from sataxi.finance.http.handlers.instalment_breakdown_lookup_handler import (
    InstalmentBreakdownLookUp,
)
from sataxi.finance.http.handlers.insurance_handler_lookup import (
    GetInsuranceBrokerByName,
    GetAllInsuranceBrokers,
    GetInsuranceCompanyByName,
    GetAllInsuranceCompanies,
)
from sataxi.finance.http.handlers.loan_account_lookup_handler import (
    LoanAccountLookup,
    LoanAccountDetailLookup,
    GetCollectSmartClientDetails,
)
from sataxi.finance.http.handlers.lookup.agreement_handler_lookup import (
    GetAllAgreements,
    GetAgreementByDescription,
)
from sataxi.finance.http.handlers.lookup.article_handler_lookup import (
    GetAllArticleTypes,
    GetArticleTypeByType,
)
from sataxi.finance.http.handlers.lookup.dealer_handler_lookup import (
    GetAllDealerCodes,
    GetDealerCodeByCode,
)
from sataxi.finance.http.handlers.lookup.employment_handler_lookup import (
    GetEmployerIndustryTypeByType,
    GetAllEmployerIndustryTypes,
)
from sataxi.finance.http.handlers.lookup.language_handler_lookup import (
    GetLanguageByDescription,
    GetAllLanguages,
)
from sataxi.finance.http.handlers.lookup.location_handler_lookup import (
    GetCountryByName,
    GetAllCountries,
    GetAreaByName,
    GetAllAreas,
)
from sataxi.finance.http.handlers.lookup.occupation_handler_lookup import (
    GetOccupationByOccupation,
    GetAllOccupations,
)
from sataxi.finance.http.handlers.lookup.relation_handler_lookup import (
    GetRelationByRelative,
    GetAllRelations,
)
from sataxi.finance.http.handlers.lookup.sale_handler_lookup import (
    GetTypeOfSaleByType,
    GetAllTypeOfSales,
)
from sataxi.finance.http.handlers.signio_handler import (
    SubmitLoanApplication,
    SaveLoanApplication,
    GetLoanDetails,
)
from sataxi.finance.http.handlers.transaction_history_handler import (
    GetTransactionHistory,
)
from sataxi.finance.http.handlers.zaka_lead_handler import GetLeadDetails

logging.getLogger(
    "bbdcommon.tornadohelpers.app_service.health_check_handler.HealthCheckHandler"
).setLevel(logging.WARNING)
DEFAULT_PORT = 8080


class FinanceService(AppServiceBase):
    def __init__(self, port, spec=None):
        self.node = PyNode()
        super().__init__(port=port, spec=spec)

    def get_url_mappings(self):
        return [
            (r"/acquire/acquire_statement/", AcquireStatement),
            (r"/acquire/acquire_settlement/", AcquireSettlement),
            (r"/acquire/acquire_notice_settlement/", AcquireNoticeSettlement),
            (r"/acquire/insurance_claim/", AcquireInsuranceClaim),
            (r"/signio/save_loan_application/", SaveLoanApplication),
            (r"/signio/submit_loan_application/", SubmitLoanApplication),
            (r"/signio/loan_details/", GetLoanDetails),
            (r"/zaka/lead_details/", GetLeadDetails),
            (r"/hive/loan_account/", LoanAccountLookup),
            (r"/hive/loan_details/", LoanAccountDetailLookup),
            (r"/hive/instalment_breakdown/", InstalmentBreakdownLookUp),
            (r"/hive/banking_details/", BankingDetailsLookup),
            (r"/client/fetch_transaction_history/", GetTransactionHistory),
            (r"/client/fetch_collectsmart_details/", GetCollectSmartClientDetails),
            (r"/client/fetch_ptp_details/", GetPTPDetailsHandler),
            (r"/client/fetch_campaign_details/", GetCampaignDetailsHandler),
            (r"/documents/available_documents/", DocumentsHandler),
            (
                r"/gomo/documents/{account_number}/available_documents/",
                GDocumentsHandler,
            ),
            (r"/gomo/loan_details/{account_number}", VGDetailsLoanGomoHandler),
            (r"/gomo/loan_validation/", VGValidationLoanGomoHandler),
            (
                r"/gomo/get_statement_details/{account_number}",
                VGGomoGetStatementDetailsHandler,
            ),
            (
                r"/gomo/loan_installment_details/{account_number}",
                VGDetailsLoanInstallmentGomoHandler,
            ),
            # LOOKUPS
            (r"/lookup/agreements/", GetAllAgreements),
            (r"/lookup/agreement_by_description/", GetAgreementByDescription),
            (r"/lookup/article_types/", GetAllArticleTypes),
            (r"/lookup/article_type_by_type/", GetArticleTypeByType),
            (r"/lookup/banks/", GetAllBanks),
            (r"/lookup/bank_by_name/", GetBankByName),
            (r"/lookup/client_types/", GetAllClientTypes),
            (r"/lookup/client_type_by_type/", GetClientTypeByType),
            (r"/lookup/dealer_codes/", GetAllDealerCodes),
            (r"/lookup/dealer_code_by_code/", GetDealerCodeByCode),
            (r"/lookup/employer_industry_types/", GetAllEmployerIndustryTypes),
            (r"/lookup/employer_industry_type_by_type/", GetEmployerIndustryTypeByType),
            (r"/lookup/insurance_companies/", GetAllInsuranceCompanies),
            (r"/lookup/insurance_company_by_name/", GetInsuranceCompanyByName),
            (r"/lookup/insurance_brokers/", GetAllInsuranceBrokers),
            (r"/lookup/insurance_broker_by_name/", GetInsuranceBrokerByName),
            (r"/lookup/languages/", GetAllLanguages),
            (r"/lookup/language_by_description/", GetLanguageByDescription),
            (r"/lookup/areas/", GetAllAreas),
            (r"/lookup/area_by_name/", GetAreaByName),
            (r"/lookup/countries/", GetAllCountries),
            (r"/lookup/country_by_name/", GetCountryByName),
            (r"/lookup/occupations/", GetAllOccupations),
            (r"/lookup/occupation_by_occupation/", GetOccupationByOccupation),
            (r"/lookup/relations/", GetAllRelations),
            (r"/lookup/relation_by_relative/", GetRelationByRelative),
            (r"/lookup/type_of_sales/", GetAllTypeOfSales),
            (r"/lookup/type_of_sale_by_type/", GetTypeOfSaleByType),
        ]


def main():
    service = FinanceService(port=DEFAULT_PORT)
    output_path = os.path.join(
        os.path.dirname(__file__), "finance_service_apispec.yaml"
    )
    with open(output_path, "w") as fw:
        fw.writelines(service.get_open_api_schema(True))
    if "--spec_only" in sys.argv:
        sys.exit(0)
    service.start_with_ioloop()


if __name__ == "__main__":
    main()
