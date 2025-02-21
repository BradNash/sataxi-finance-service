from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.common.schemas.banking_details_schema import (
    BankingDetailsLookupResponse,
)
from sataxi.finance.db.sqlalchemy.db_VG_View_Loan_BankDetails import (
    DB_VG_View_Loan_BankDetailsSelectBankingDetails,
)


def get_banking_details(session: Session, bank_ref: str):
    banking_details = DB_VG_View_Loan_BankDetailsSelectBankingDetails.execute(
        session, bank_ref
    )

    banking_details_list: List[BankingDetailsLookupResponse] = []
    for banking_detail in banking_details:
        banking_details_list.append(
            BankingDetailsLookupResponse(
                banking_detail.BankName,
                banking_detail.BranchType,
                banking_detail.AccountNo,
                banking_detail.Expr1,
                banking_detail.BankReference,
            )
        )
    return banking_details_list
