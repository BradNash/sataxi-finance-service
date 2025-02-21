"""Module providing schema for documents."""
from dataclasses import dataclass
from enum import Enum
from typing import List

from bbdcommon.spechelpers.misc import schema_field


class Company(Enum):
    """Class representing a company"""

    SAT = "SA taxi development finance"
    GOMO = "Gomo vehicle finance"


class Department(Enum):
    """Class representing a Department"""
    SAT_CSC = "Customer Service Center"
    GOMO_GFS = "Gomo Financial Services"
    GOMO_GVS = "Gomo Vehicle Services"


class Language(Enum):
    """Class representing a document language"""

    ENG = "English"


@dataclass
class AvailableDocuments(Enum):
    """Class representing documents that are available with their attributes"""

    # SAT-CSC
    CONFIRMATION_OF_FINANCE = "Confirmation Of Finance", Language.ENG, [Company.SAT]
    CONFIRMATION_OF_PAYMENTS = (
        "Confirmation of Payment Made in Full - All Structures",
        Language.ENG,
        [Company.SAT],
        [Department.SAT_CSC],
    )
    PAYMENTS_UP_TO_DATE = (
        "Payments Up To Date - Confirmation that Account is not in arrears",
        Language.ENG,
        [Company.SAT],
        [Department.SAT_CSC],
    )
    CROSS_BOARDER_LETTER = (
        "SA Taxi - Cross Boarder Letter - All Funding Structures",
        Language.ENG,
        [Company.SAT],
        [Department.SAT_CSC],
    )
    THIRD_PARTY_CONSENT = "Third Party Consent", Language.ENG, [Company.SAT]
    CHANGE_OF_INSTALMENT_DATE = "Change Of Instalment Date", Language.ENG, [Company.SAT]
    DEBIT_ORDER_AUTHORITY_FORM = (
        "Debit Order Authority Form",
        Language.ENG,
        [Company.SAT],
        [Department.SAT_CSC],
    )
    REQUEST_OF_ENATIS = "Request of Enatis", Language.ENG, [Company.SAT]
    REQUEST_FOR_BANKING_DETAILS = (
        "Request For Banking Details",
        Language.ENG,
        [Company.SAT],
        [Department.SAT_CSC],
    )
    REFUND_CHECKLIST = "Refund Checklist", Language.ENG, [Company.SAT], [Department.SAT_CSC]
    SETTLEMENT_CHECKLIST = "Settlement Checklist", Language.ENG, [Company.SAT], [Department.SAT_CSC]
    # GOMO-GFS
    SUBSTITUTION_ADDENDUM_GFS = "Substitution Addendum letter", Language.ENG, [Company.GOMO], [Department.GOMO_GFS]
    # ADDENDUM_TERM_RATE = "Addendum term rate letter", Language.ENG, [Company.GOMO]
    AUTHORISATION_OF_GOODS_GFS = (
        "Authorisation of goods letter",
        Language.ENG,
        [Company.GOMO],
        [Department.GOMO_GFS]
    )
    NOTICE_OF_DEMAND_GFS = "Notice of demand letter", Language.ENG, [Company.GOMO], [Department.GOMO_GFS]
    BORDER_LETTER_GFS = "Cross border letter", Language.ENG, [Company.GOMO], [Department.GOMO_GFS]
    CONFIRMATION_OF_OWNERSHIP_GFS = (
        "Ownership confirmation letter",
        Language.ENG,
        [Company.GOMO],
        [Department.GOMO_GFS]
    )
    INTEREST_RATE_ADJUSTMENT_GFS = (
        "Interest rate change letter",
        Language.ENG,
        [Company.GOMO],
        [Department.GOMO_GFS]
    )
    LETTER_NO_INTEREST_GFS = "Letter of no interest", Language.ENG, [Company.GOMO], [Department.GOMO_GFS]
    PAID_IN_FULL_GFS = "Paid in full letter", Language.ENG, [Company.GOMO], [Department.GOMO_GFS]
    PART_REPLACEMENT_GFS = "Parts replacement letter", Language.ENG, [Company.GOMO], [Department.GOMO_GFS]
    # GOMO-GVS
    SUBSTITUTION_ADDENDUM_GVS = "Substitution Addendum letter", Language.ENG, [Company.GOMO], [Department.GOMO_GVS]
    # ADDENDUM_TERM_RATE = "Addendum term rate letter", Language.ENG, [Company.GOMO]
    AUTHORISATION_OF_GOODS_GVS = (
        "Authorisation of goods letter",
        Language.ENG,
        [Company.GOMO],
        [Department.GOMO_GVS]
    )
    NOTICE_OF_DEMAND_GVS = "Notice of demand letter", Language.ENG, [Company.GOMO], [Department.GOMO_GVS]
    BORDER_LETTER_GVS = "Cross border letter", Language.ENG, [Company.GOMO], [Department.GOMO_GVS]
    CONFIRMATION_OF_OWNERSHIP_GVS = (
        "Ownership confirmation letter",
        Language.ENG,
        [Company.GOMO],
        [Department.GOMO_GVS]
    )
    INTEREST_RATE_ADJUSTMENT_GVS = (
        "Interest rate change letter",
        Language.ENG,
        [Company.GOMO],
        [Department.GOMO_GVS]
    )
    LETTER_NO_INTEREST_GVS = "Letter of no interest", Language.ENG, [Company.GOMO], [Department.GOMO_GVS]
    PAID_IN_FULL_GVS = "Paid in full letter", Language.ENG, [Company.GOMO], [Department.GOMO_GVS]
    PART_REPLACEMENT_GVS = "Parts replacement letter", Language.ENG, [Company.GOMO], [Department.GOMO_GVS]


@dataclass
class Documents:
    """Class representing a document with its properties"""

    def __init__(self):
        self.identifier = ""
        self.document_name = ""
        self.reason = ""
        self.disabled = False
        self.language = Language.ENG
        self.company_name = List[Company]

    identifier: str = schema_field(data_key="identifier")
    document_name: str = schema_field(data_key="documentName")
    reason: str = schema_field(data_key="reason")
    disabled: bool = schema_field(data_key="disabled", default=False)


@dataclass
class DocumentsResponse:
    """Class representing the response of available documents"""

    def __init__(self):
        self.documents = []
        self.stamp = bytearray()

    documents: List[Documents] = schema_field(data_key="documents")
    stamp: bytes = schema_field(data_key="stampData")
    footer: str = schema_field(data_key="footer")


def get_document_name(document: AvailableDocuments):
    return document.value[0]


def get_document_language(document: AvailableDocuments):
    return document.value[1]


def get_document_company(document: AvailableDocuments):
    return document.value[2]


def get_document_department(document: AvailableDocuments):
    return document.value[3]


def set_document(doc: AvailableDocuments) -> Documents:
    document = Documents()
    document.identifier = doc.name
    document.document_name = get_document_name(doc)
    document.company_name = get_document_company(doc)

    return document
