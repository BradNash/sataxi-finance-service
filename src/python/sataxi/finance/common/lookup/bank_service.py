from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.db.sqlalchemy.db_Bank import (
    DB_BankDeleteOne,
    DB_BankInsert,
    DB_BankSelectAll,
    DB_BankSelectByBankName,
    DB_BankSelectOne,
    DB_BankUpdate,
)


def get_all_banks(session: Session) -> List[DB_BankSelectAll]:
    return DB_BankSelectAll.execute(session)


def get_bank_by_name(session: Session, bank_name: str) -> DB_BankSelectByBankName:
    return DB_BankSelectByBankName.execute(session, bank_name)


def get_bank_by_id(session: Session, bank_id: int):
    return DB_BankSelectOne.execute(session, bank_id)


def insert_bank(session: Session, bank_name: str):
    return DB_BankInsert.execute(session, bank_name)


def update_bank(session: Session, bank_name: str, bank_id: int):
    return DB_BankUpdate.execute(session, bank_name, bank_id)


def delete_bank_by_id(session: Session, bank_int: int):
    return DB_BankDeleteOne.execute(session, bank_int)
