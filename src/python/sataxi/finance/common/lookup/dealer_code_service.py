from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.db.sqlalchemy.db_DealerCode import (
    DB_DealerCodeDeleteOne,
    DB_DealerCodeInsert,
    DB_DealerCodeSelectAll,
    DB_DealerCodeSelectByCode,
    DB_DealerCodeSelectOne,
    DB_DealerCodeUpdate,
)


def get_all_dealer_codes(session: Session) -> List[DB_DealerCodeSelectAll]:
    return DB_DealerCodeSelectAll.execute(session)


def get_dealer_code_by_code(session: Session, code: str) -> DB_DealerCodeSelectByCode:
    return DB_DealerCodeSelectByCode.execute(session, code)


def get_dealer_code_by_id(session: Session, code_id: int):
    return DB_DealerCodeSelectOne.execute(session, code_id)


def insert_dealer_code(session: Session, code: str):
    return DB_DealerCodeInsert.execute(session, code)


def update_dealer_code(session: Session, code: str, code_id: int):
    return DB_DealerCodeUpdate.execute(session, code, code_id)


def delete_dealer_code_by_id(session: Session, code_id: int):
    return DB_DealerCodeDeleteOne.execute(session, code_id)
