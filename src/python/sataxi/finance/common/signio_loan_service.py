import json
import logging
import os
import uuid
import xml.etree.ElementTree as elm_tree
from datetime import datetime

import rsaidnumber
import tornado.httpclient
from bbdcommon.tornadohelpers.base.proto import AppProto
from marshmallow_dataclass import class_schema
from sqlalchemy.orm import Session
from tornado.httpclient import HTTPError

from sataxi.finance.common.schemas.default_configs import SignioConfigs
from sataxi.finance.common.schemas.signio_schema import (
    AppDetails,
    ApplicantExpenses,
    ApplicantIncome,
    Application,
    BankStatementConsent,
    BankingDetails,
    BeeActStatus,
    EmployerDetails,
    FinanceDetails,
    LiabilityDetails,
    PassportDetails,
    PaymentHistory,
    PersonalDetails,
    RelativeDetails,
    ResidentialDetails,
    SataxiInsurance,
    SataxiRoute,
    SourceOfFunds,
    SpouseDetails,
    Statement,
    VehicleDetails,
    Campaign,
)
from sataxi.finance.common.schemas.signio_schema import SignioLoanDetailsRequest
from sataxi.finance.common.utils.config_http_wrapper import ConfigHttpWrapper
from sataxi.finance.db.sqlalchemy.db_SignioLoanApplication import (
    DB_SignioLoanApplicationInsert,
    DB_SignioLoanApplicationSelectOneUpd,
)
from sataxi.finance.db.sqlalchemy.db_SignioLoanDetails import (
    DB_SignioLoanDetailsInsert,
    DB_SignioLoanDetailsUpdate,
    DB_SignioLoanDetailsSelectOneUpd,
)
from sataxi.finance.db.sqlalchemy.db_SignioLoanDetails import (
    DB_SignioLoanDetailsSelectOne,
)
from sataxi.finance.db.sqlalchemy.db_VG_Leads_ABL import DB_VG_Leads_ABLSelectByIdNumber
from sataxi.finance.messaging.events.sigino_application import (
    SignioApplicationGeneratedV1,
)


def save_signio_loan_details(
    session: Session, signio_loan_details: SignioLoanDetailsRequest
):

    existing_application = DB_SignioLoanDetailsSelectOne.execute(
        session, signio_loan_details.caseNumber
    )
    if existing_application is None:
        DB_SignioLoanDetailsInsert.execute(
            session,
            signio_loan_details.caseNumber,
            signio_loan_details.to_json(),
            int(signio_loan_details.campaign.value),
            0,
            None,
        )
    else:
        DB_SignioLoanDetailsUpdate.execute(
            session,
            signio_loan_details.to_json(),
            int(signio_loan_details.campaign.value),
            int(existing_application.processed),
            existing_application.processed_date,
            signio_loan_details.caseNumber,
        )


def export_signio_application_to_excel(
    application: AppProto,
    signio_loan_details_request: SignioLoanDetailsRequest,
    current_user: str,
):
    signio_dict = class_schema(SignioLoanDetailsRequest)().dump(
        signio_loan_details_request
    )
    user_specified_key = str(uuid.uuid4())
    custormer_idnumber = signio_loan_details_request.eApplication.customerIdNumber
    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    signio_application_generated = SignioApplicationGeneratedV1(
        content_type=2,
        source_type=1,
        source_id="UploadContentV1",
        user=current_user,
        user_specified_key=user_specified_key,
        file_name=f"signio_application_" f"{custormer_idnumber}.xlsx",
        mime_type=mime_type,
        encryption_password=None,
        signio_application_data=signio_dict,
    )
    application.server_base.node.bus.send(
        msg_obj=signio_application_generated, reply_node_id=None
    )
    application.server_base.node.bus.commit_messaging()
    application.server_base.node.bus.emit_prompts()
    application.server_base.node.bus.reset_state()


async def submit_signio_application(
    session: Session,
    application: AppProto,
    signio_loan_details: SignioLoanDetailsRequest,
):
    http_wrapper = ConfigHttpWrapper()
    signio_configs: SignioConfigs = __populate_defaults(application)
    existing_application = DB_SignioLoanDetailsSelectOneUpd.execute(
        session, signio_loan_details.caseNumber
    )
    if existing_application is None:
        DB_SignioLoanDetailsInsert.execute(
            session,
            signio_loan_details.caseNumber,
            signio_loan_details.to_json(),
            int(signio_loan_details.campaign.value),
            0,
            None,
        )
    else:
        DB_SignioLoanDetailsUpdate.execute(
            session,
            signio_loan_details.to_json(),
            int(signio_loan_details.campaign.value),
            int(existing_application.processed),
            existing_application.processed_date,
            signio_loan_details.caseNumber,
        )

    try:
        # MAP XML FROM REQUEST PAYLOAD
        xml = generate_signio_xml(signio_configs, signio_loan_details)
        signio_application = DB_SignioLoanApplicationSelectOneUpd.execute(
            session, signio_loan_details.caseNumber
        )

        # SEND XML TO SIGNIO
        res = await http_wrapper.submit_3rd_party_application(signio_configs, xml)
        body = json.loads(res.body.decode("utf-8"))
        # SAVE SIGNIO REQUEST & RESPONSE. IF 200 UPDATE APP TO PROCESSED = 1
        if signio_application is None:
            DB_SignioLoanApplicationInsert.execute(
                session,
                signio_loan_details.caseNumber,
                xml,
                body["results"]["message"],
                res.code,
                body["results"]["referenceNumber"],
            )
            DB_SignioLoanDetailsUpdate.execute(
                session,
                signio_loan_details.to_json(),
                int(signio_loan_details.campaign.value),
                1,
                datetime.now(),
                signio_loan_details.caseNumber,
            )
        else:
            DB_SignioLoanDetailsUpdate.execute(
                session,
                signio_loan_details.to_json(),
                int(signio_loan_details.campaign.value),
                1,
                existing_application.processed_date,
                signio_loan_details.caseNumber,
            )

    except HTTPError as e:
        raise tornado.httpclient.HTTPError(
            code=e.code,
            message=json.loads(e.response.body.decode("utf-8"))["results"]["error"],
        )


def __populate_defaults(application) -> SignioConfigs:
    signio_configs = application.server_base.config.get("SignioInfo")
    return SignioConfigs(
        signio_configs.get("URL"),
        signio_configs.get("AuthToken"),
        signio_configs.get("Authorization"),
        signio_configs.get("DealerCodes"),
    )


def generate_signio_xml(
    signio_configs: SignioConfigs, signio_loan_details: SignioLoanDetailsRequest
):
    tree = elm_tree.parse(
        os.path.dirname(__file__) + "/payloads/xml/sataxi_xml_template.xml"
    )
    data_bundle = tree.getroot().find("dataBundle")

    if signio_loan_details.campaign.value == "TRADE_UP":
        dealer_code: str = signio_configs.dealer_codes[0]["TradeUp"]
    else:
        dealer_code: str = signio_configs.dealer_codes[1]["Zaka"]
    data_bundle.append(
        elm_tree.fromstring(
            '<field formFieldName="{}">{}</field>'.format(
                "thirdPartyVendorCode", dealer_code
            )
        )
    )
    for key, value in signio_loan_details.__dict__.items():
        if key != "caseNumber" and key != "campaign" and value is not None:
            for k, v in value.__dict__.items():
                if type(v) == bool:
                    v = "Yes" if v else "No"
                # if type(v) == str:
                #     v = v.upper()
                print(f"k-{k}, v-{v}")
                # print(data_bundle.items())
                data_bundle.append(
                    elm_tree.fromstring(
                        '<field formFieldName="{}">{}</field>'.format(k, v)
                    )
                )
    formated_xml = elm_tree.tostring(
        tree.getroot(), encoding="utf-8", method="xml"
    ).decode("utf-8")
    return formated_xml


def fetch_loan_details(hive_session: Session, id_number: str):
    logging.debug("Using HIVE Data from")
    hive_details = DB_VG_Leads_ABLSelectByIdNumber.execute(hive_session, id_number)

    signio_loan_details_request = assign_hive_loan_details(hive_details[0])
    return signio_loan_details_request


def assign_hive_loan_details(hive_details: DB_VG_Leads_ABLSelectByIdNumber):
    identity_obj = rsaidnumber.parse(hive_details.IDNumber)

    e_application: Application = Application()
    name = hive_details.customerFirstName.strip().split(" ")
    e_application.customerFirstName = hive_details.customerFirstName.strip()
    e_application.customerMiddleName = name[1] if len(name) > 1 else ""
    e_application.customerSurname = hive_details.customerSurname.strip()
    e_application.customerIdNumber = hive_details.IDNumber.strip()
    e_application.customerDateOfBirth = identity_obj.date_of_birth.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    vehicle_details: VehicleDetails = VehicleDetails()
    vehicle_details.make = hive_details.Make
    vehicle_details.vehicleDescription = hive_details.Model
    vehicle_details.engineNumber = hive_details.engineNumber
    vehicle_details.vehicleNumberOfSeats = (
        int(hive_details.SeatNumber[0:2]) if hive_details.SeatNumber else 0
    )
    vehicle_details.typeOfSale = hive_details.typeOfSale
    vehicle_details.yearModel = hive_details.YearOfManufature
    vehicle_details.chassisNo = hive_details.ChassisNumber

    personal_details: PersonalDetails = PersonalDetails()
    personal_details.customerGender = identity_obj.gender
    personal_details.customerNationality = identity_obj.citizenship
    personal_details.customerMobilePhoneNumber = hive_details.ContactDetails
    personal_details.customerTitle = hive_details.Title

    residential_address: ResidentialDetails = ResidentialDetails()
    address = hive_details.residentialDetails
    last_index_of_comma = address.rindex(",") if address else 0
    residential_address.customerResidentialAddressLine1 = (
        address[0:last_index_of_comma] if address else ""
    )
    residential_address.customerResidentialAddressPostalCode = (
        address[last_index_of_comma + 1 :] if address else ""
    )
    residential_address.customerPostalAddressLine1 = (
        address[0:last_index_of_comma] if address else ""
    )
    residential_address.customerPostalAddressPostalCode = (
        address[last_index_of_comma + 1 :] if address else ""
    )

    sataxi_route: SataxiRoute = SataxiRoute()
    sataxi_route.taxiAssociation = hive_details.taxiAssociation
    sataxi_route.routeFromTo = hive_details.routeFromTo or ""
    sataxi_route.taxiAssociationProvince = hive_details.Province
    sataxi_route.kmPerTrip = hive_details.kmPerTrip
    sataxi_route.noOfTripsPerDay = hive_details.TripsPerDay
    sataxi_route.monIncNoOfSeats = (
        int(hive_details.SeatNumber[0:2]) if hive_details.SeatNumber else 0
    )

    sataxi_insurance: SataxiInsurance = SataxiInsurance()
    sataxi_insurance.supplier = hive_details.supplier
    sataxi_insurance.insuranceBroker = hive_details.insuranceBroker
    sataxi_insurance.insuranceAmount = float(hive_details.insuranceAmount)

    finance_details: FinanceDetails = FinanceDetails()
    passport_details: PassportDetails = PassportDetails()
    spouse_details: SpouseDetails = SpouseDetails()
    employer_details: EmployerDetails = EmployerDetails()
    applicant_income: ApplicantIncome = ApplicantIncome()
    applicant_expenses: ApplicantExpenses = ApplicantExpenses()
    source_of_funds: SourceOfFunds = SourceOfFunds()
    liability_details: LiabilityDetails = LiabilityDetails()
    payment_history: PaymentHistory = PaymentHistory()
    relative_details: RelativeDetails = RelativeDetails()
    banking_details: BankingDetails = BankingDetails()
    statement: Statement = Statement()
    app_details: AppDetails = AppDetails()
    bank_statement_consent: BankStatementConsent = BankStatementConsent()
    bee_act_status: BeeActStatus = BeeActStatus()

    latest_details: SignioLoanDetailsRequest = SignioLoanDetailsRequest(
        1,
        Campaign.__getitem__(hive_details.Campaign.upper()),
        e_application,
        vehicle_details,
        finance_details,
        personal_details,
        residential_address,
        passport_details,
        spouse_details,
        employer_details,
        applicant_income,
        applicant_expenses,
        source_of_funds,
        liability_details,
        payment_history,
        relative_details,
        banking_details,
        statement,
        app_details,
        bank_statement_consent,
        sataxi_route,
        sataxi_insurance,
        bee_act_status,
    )

    return latest_details
