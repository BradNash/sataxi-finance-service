from sqlalchemy.orm import Session
from sataxi.finance.common.schemas.vg_gomo_get_statement_details_schema import (
    VGGomoGetStatementDetailsResponse,
)

from sataxi.finance.db.sqlalchemy.db_VG_GomoGetStatementDetails import (
    DB_VG_GomoGetStatementDetailsSelectByAccountNumber,
)
from typing import List


def gomo_get_statement_details(session: Session, account_number: str):
    statement_details = DB_VG_GomoGetStatementDetailsSelectByAccountNumber.execute(
        session, account_number
    )
    statement_details_list: List[VGGomoGetStatementDetailsResponse] = []

    for statement in statement_details:
        statement_details_list.append(
            VGGomoGetStatementDetailsResponse(
                # Note: Rounding Money values to remove floating point errors in DB values.
                # If else required to catch if value is Null in DB
                statement.RowNo,
                statement.AccountNumber,
                statement.PostDate,
                statement.EffectiveDate,
                statement.TransactionType,
                statement.Narrative,
                round(statement.DebitAmount, 2)
                if statement.DebitAmount is not None
                else statement.DebitAmount,
                round(statement.CreditAmount, 2)
                if statement.CreditAmount is not None
                else statement.CreditAmount,
                statement.CustomerAccountType,
                statement.SimplifiedDescription,
                round(statement.ArrearsBalance, 2)
                if statement.ArrearsBalance is not None
                else statement.ArrearsBalance,
                round(statement.CapitalBalance, 2)
                if statement.CapitalBalance is not None
                else statement.CapitalBalance,
                round(statement.TotalBalance, 2)
                if statement.TotalBalance is not None
                else statement.TotalBalance,
                statement.IDNumber,
            )
        )

    return statement_details_list
