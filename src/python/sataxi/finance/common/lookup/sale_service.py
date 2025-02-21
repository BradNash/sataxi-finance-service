from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.db.sqlalchemy.db_TypeOfSale import (
    DB_TypeOfSaleDeleteOne,
    DB_TypeOfSaleInsert,
    DB_TypeOfSaleSelectAll,
    DB_TypeOfSaleSelectByType,
    DB_TypeOfSaleSelectOne,
    DB_TypeOfSaleUpdate,
)


def get_all_type_of_sales(session: Session) -> List[DB_TypeOfSaleSelectAll]:
    return DB_TypeOfSaleSelectAll.execute(session)


def get_type_of_sale_by_type(session: Session, type: str) -> DB_TypeOfSaleSelectByType:
    return DB_TypeOfSaleSelectByType.execute(session, type)


def get_type_of_sale_by_id(session: Session, type_id: int):
    return DB_TypeOfSaleSelectOne.execute(session, type_id)


def insert_type_of_sale(session: Session, type: str):
    return DB_TypeOfSaleInsert.execute(session, type)


def update_type_of_sale(session: Session, type: str, type_id: int):
    return DB_TypeOfSaleUpdate.execute(session, type, type_id)


def delete_type_of_sale_by_id(session: Session, type_id: int):
    return DB_TypeOfSaleDeleteOne.execute(session, type_id)
