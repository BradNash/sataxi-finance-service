from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.common.schemas.transaction_history_schema import (
    TransactionHistoryResponse,
)
from sataxi.finance.db.sqlalchemy.db_Acquire_View_GetStatementDetails import (
    DB_Acquire_View_GetStatementDetailsSelectTransactionHistory,
)


def get_transaction_history(session: Session, account_number: str):
    transaction_history = (
        DB_Acquire_View_GetStatementDetailsSelectTransactionHistory.execute(
            session, account_number
        )
    )

    transactions: List[TransactionHistoryResponse] = []
    for t in transaction_history:
        transactions.append(
            TransactionHistoryResponse(
                t.accountNumber,
                t.postDate,
                t.effectiveDate,
                t.transactionType,
                t.narrative,
                t.transactionAmount,
                t.customerAccountType,
                t.capitalBalance,
                t.arrearsBalance,
                t.totalBalance,
                t.structureName,
            )
        )
    return transactions
