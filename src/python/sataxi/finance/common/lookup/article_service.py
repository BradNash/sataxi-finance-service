from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.db.sqlalchemy.db_ArticleType import (
    DB_ArticleTypeDeleteOne,
    DB_ArticleTypeInsert,
    DB_ArticleTypeSelectAll,
    DB_ArticleTypeSelectByType,
    DB_ArticleTypeSelectOne,
    DB_ArticleTypeUpdate,
)


def get_all_article_types(session: Session) -> List[DB_ArticleTypeSelectAll]:
    return DB_ArticleTypeSelectAll.execute(session)


def get_article_type_by_type(session: Session, type: str) -> DB_ArticleTypeSelectByType:
    return DB_ArticleTypeSelectByType.execute(session, type)


def get_article_type_by_id(session: Session, type_id: str):
    return DB_ArticleTypeSelectOne.execute(session, type_id)


def insert_article_type(session: Session, type: str):
    return DB_ArticleTypeInsert.execute(session, type)


def update_article_type(session: Session, type: str, type_id: int):
    return DB_ArticleTypeUpdate.execute(session, type, type_id)


def delete_article_type_by_id(session: Session, type_id: str):
    return DB_ArticleTypeDeleteOne.execute(session, type_id)
