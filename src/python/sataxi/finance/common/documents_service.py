"""Module providing business rules for documents."""
import base64
import logging
import os
from typing import List

import yaml
from sqlalchemy.orm import Session

from sataxi.finance.common.schemas.documents_schema import (
    AvailableDocuments,
    DocumentsResponse,
    Documents,
    Company, get_document_company, set_document, Department, get_document_department,
)
from sataxi.finance.db.sqlalchemy import (
    DB_VG_Details_LoanSelectClientDetails,
    DB_Acquire_View_GetStatementDetailsSelectTransactionHistoryByType,
    DB_VG_Details_Loan_GomoSelectByAccountNumber,
    DB_VG_Details_LoanInstalment_GomoSelectByAccountNumber,
)


def get_available_documents_for_client(
    session: Session, account_number: str, company: Company
) -> DocumentsResponse:
    document_response = DocumentsResponse()

    if company == Company.GOMO:
        vg_details_loan: List[
            DB_VG_Details_Loan_GomoSelectByAccountNumber
        ] = DB_VG_Details_Loan_GomoSelectByAccountNumber.execute(
            session, account_number
        )

        vg_loan_installments: List[
            DB_VG_Details_LoanInstalment_GomoSelectByAccountNumber
        ] = DB_VG_Details_LoanInstalment_GomoSelectByAccountNumber.execute(
            session, account_number
        )

        document_response.documents.extend(
            availability_rules(vg_details_loan[0], vg_loan_installments, Company.GOMO)
        )

    else:
        vg_details_loan: DB_VG_Details_LoanSelectClientDetails = (
            DB_VG_Details_LoanSelectClientDetails.execute(session, account_number)
        )

        vg_loan_installments: List[
            DB_Acquire_View_GetStatementDetailsSelectTransactionHistoryByType
        ] = DB_Acquire_View_GetStatementDetailsSelectTransactionHistoryByType.execute(
            session, "INS", account_number
        )
        vg_loan_installments.extend(
            DB_Acquire_View_GetStatementDetailsSelectTransactionHistoryByType.execute(
                session, "INSE", account_number
            )
        )

        document_response.documents.extend(
            availability_rules(vg_details_loan, vg_loan_installments, Company.SAT)
        )

        footer_identifier, stamp_data = determine_stamp_and_footer(vg_details_loan)
        document_response.stamp = base64.b64encode(stamp_data.read()).decode("utf-8")
        stamp_data.close()
        document_response.footer = determine_footer(footer_identifier)

    return document_response


def determine_stamp_and_footer(vg_details_loan):
    stamps_path = os.path.abspath(
        os.path.realpath(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "./configs/stamps//"
            )
        )
    )
    footer_identifier = str
    if vg_details_loan.CompanyName == "SA Taxi Impact Fund (Pty) Ltd":
        stamp_data = open(stamps_path + "/SATAXI_IMPACT_FUND.png", "rb")
        footer_identifier = "SATAXI_IMPACT_FUND"

    elif vg_details_loan.CompanyName == "SA Taxi Securitisation (Pty) Ltd":
        stamp_data = open(stamps_path + "/SATAXI_SECURITISATION.png", "rb")
        footer_identifier = "SATAXI_SECURITISATION"

    elif vg_details_loan.CompanyName == "SA Taxi Development Finance (Pty) Ltd":
        stamp_data = open(stamps_path + "/SATAXI_DEV_FINANCE.png", "rb")
        footer_identifier = "SATAXI_DEV_FINANCE"

    elif vg_details_loan.CompanyName.__contains__("Transflow"):
        stamp_data = open(stamps_path + "/TRANSFLOW_PTY_LTD.png", "rb")
        footer_identifier = "TRANSFLOW_PTY_LTD"

    elif vg_details_loan.CompanyName.__contains__("Transsec"):
        stamp_data = open(stamps_path + "/TRANSSEC.png", "rb")
        if vg_details_loan.CompanyName.__contains__("Transsec 2"):
            footer_identifier = "TRANSSEC2"
        elif vg_details_loan.CompanyName.__contains__("Transsec 3"):
            footer_identifier = "TRANSSEC3"
        elif vg_details_loan.CompanyName.__contains__("Transsec 4"):
            footer_identifier = "TRANSSEC4"
        elif vg_details_loan.CompanyName.__contains__("Transsec 5"):
            footer_identifier = "TRANSSEC5"
        else:
            footer_identifier = "TRANSSEC"

    elif vg_details_loan.CompanyName.__contains__("Potpale"):
        stamp_data = open(stamps_path + "/POTPALE_INVESTMENTS.png", "rb")
        footer_identifier = "POTPALE_INVESTMENTS"

    elif vg_details_loan.CompanyName == "SA Taxi Finance Solutions (Pty) Ltd":
        stamp_data = open(stamps_path + "/SATAXI_FINANCE_SOLUTION.png", "rb")
        footer_identifier = "SATAXI_FINANCE_SOLUTION"

    else:
        stamp_data = open(stamps_path + "/CERTIFIED_COPY_OF_DOCUMENT_SIGNED.png", "rb")
    return footer_identifier, stamp_data


def availability_rules(
    vg_details_loan: any, vg_loan_installments: [], company: Company
) -> [Documents]:
    if Company.GOMO == company:
        return gomo_document_rules(vg_details_loan)

    if Company.SAT == company:
        return sat_document_rules(vg_details_loan, vg_loan_installments)

    logging.warning("Unknown company provided")
    return []


def sat_document_rules(vg_details_loan: any, vg_loan_installments: []) -> [Documents]:
    documents: List[Documents] = []

    for available_document in filter(
        lambda x: Company.SAT in get_document_company(x), AvailableDocuments
    ):
        document = set_document(available_document)

        if document.identifier == "CROSS_BOARDER_LETTER":
            document.disabled = (
                vg_details_loan.TotalDueCS > 0.00 or len(vg_loan_installments) <= 3
            )
            document.reason = "The account is either in arrears or there are less than 3 instalments received to date."
            documents.append(document)
            continue

        if document.identifier == "CONFIRMATION_OF_PAYMENTS":
            document.disabled = vg_details_loan.AccountStatus.upper() != "SETTLED"
            document.reason = "This account is still Active."
            documents.append(document)
            continue

        if document.identifier == "PAYMENTS_UP_TO_DATE":
            document.disabled = vg_details_loan.TotalDueCS > 0.00
            document.reason = "This account is in Arrears"
            documents.append(document)
            continue

        # This rule is same as for Confirmation of Payment
        if document.identifier == "REQUEST_OF_ENATIS":
            document.disabled = vg_details_loan.AccountStatus.upper() != "SETTLED"
            document.reason = "The status of the account is not Settled."
            documents.append(document)
            continue

        if document.identifier == "DEBIT_ORDER_AUTHORITY_FORM":
            document.disabled = vg_details_loan.PaymentMethod.upper() != "CASH"
            document.reason = "The payment method on this account is not Cash"
            documents.append(document)
            continue

        documents.append(document)
    return documents


def gomo_document_rules(vg_details_loan: any):
    documents: List[Documents] = []
    department_docs = Department.GOMO_GFS if vg_details_loan.StructureCode == "C0100-001" else Department.GOMO_GVS
    for available_document in filter(lambda x: Company.GOMO in get_document_company(x)
                                     and department_docs in get_document_department(x),
                                     AvailableDocuments):
        document = set_document(available_document)

        if document.identifier in ("BORDER_LETTER_GFS", "BORDER_LETTER_GVS"):
            document.disabled = (
                vg_details_loan.TotalDueCS > 0.00
                or vg_details_loan.AccountStatus == "SETTLED"
            )
            document.reason = (
                "The account is settled."
                if vg_details_loan.AccountStatus == "SETTLED"
                else "The account is in arrears."
            )
            documents.append(document)
            continue

        if document.identifier in ("PAID_IN_FULL_GFS", "PAID_IN_FULL_GVS", "LETTER_NO_INTEREST_GFS",
                                   "LETTER_NO_INTEREST_GVS"):
            document.disabled = vg_details_loan.AccountStatus.upper() != "SETTLED"
            document.reason = "This account is still Active."
            documents.append(document)
            continue

        if document.identifier in ("NOTICE_OF_DEMAND_GFS", "NOTICE_OF_DEMAND_GVS"):
            document.disabled = vg_details_loan.MonthsInArrears <= 0
            document.reason = "This account is not in arrears."
            documents.append(document)
            continue

        documents.append(document)
    return documents


def determine_footer(footer_identifier: str):
    footer_path = os.path.abspath(
        os.path.realpath(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "./configs/document_footer.yaml",
            )
        )
    )
    with open(footer_path, "r") as f:
        data = yaml.safe_load(f)
        return data[footer_identifier]
