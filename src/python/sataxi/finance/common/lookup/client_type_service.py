from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.db.sqlalchemy.db_ClientType import (
    DB_ClientTypeDeleteOne,
    DB_ClientTypeInsert,
    DB_ClientTypeSelectAll,
    DB_ClientTypeSelectByType,
    DB_ClientTypeSelectOne,
    DB_ClientTypeUpdate,
)


def get_all_client_types(session: Session) -> List[DB_ClientTypeSelectAll]:
    return DB_ClientTypeSelectAll.execute(session)


def get_client_type_by_type(session: Session, type: str) -> DB_ClientTypeSelectByType:
    return DB_ClientTypeSelectByType.execute(session, type)


def get_client_type_by_id(session: Session, type_id: str):
    return DB_ClientTypeSelectOne.execute(session, type_id)


def insert_client_type(session: Session, type: str):
    return DB_ClientTypeInsert.execute(session, type)


def update_client_type(session: Session, type: str, type_id: int):
    return DB_ClientTypeUpdate.execute(session, type, type_id)


def delete_client_by_id(session: Session, type_id: str):
    return DB_ClientTypeDeleteOne.execute(session, type_id)
