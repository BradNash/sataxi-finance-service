from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.common.schemas.instalment_breakdown_schema import (
    InstalmentBreakdownLookUpResponse,
)
from sataxi.finance.common.schemas.vg_details_loaninstallment_gomo import (
    VGDetailsLoanInstallmentGomoResponse,
)
from sataxi.finance.db.sqlalchemy import (
    DB_VG_Details_LoanInstalment_GomoSelectByAccountNumber,
)
from sataxi.finance.db.sqlalchemy.db_VG_Details_LoanInstalment import (
    DB_VG_Details_LoanInstalmentSelectInstalmentBreakdown,
)


def get_instalment_breakdown(session: Session, account_number: str):
    installment_breakdown = (
        DB_VG_Details_LoanInstalmentSelectInstalmentBreakdown.execute(
            session, account_number
        )
    )
    installment_breakdown_list: List[InstalmentBreakdownLookUpResponse] = []
    for installment in installment_breakdown:
        installment_breakdown_list.append(
            InstalmentBreakdownLookUpResponse(
                installment.AccountNumber,
                installment.Description,
                installment.ValueDate,
                installment.InstalmentAmount,
            )
        )
    return installment_breakdown_list


def get_gomo_loaninstallment(session: Session, account_number: str):
    loan_installments = DB_VG_Details_LoanInstalment_GomoSelectByAccountNumber.execute(
        session, account_number
    )
    loan_installment_list: List[VGDetailsLoanInstallmentGomoResponse] = []

    for installment in loan_installments:
        install = VGDetailsLoanInstallmentGomoResponse(
            # Note: Rounding Money values to remove floating point errors in DB values.
            # If else required to catch if value is Null in DB
            installment.AccountNumber,
            installment.Description,
            installment.ValueDate,
            round(installment.InstalmentAmount, 2)
            if installment.InstalmentAmount is not None
            else installment.InstalmentAmount,
        )
        loan_installment_list.append(install)

    return loan_installment_list
