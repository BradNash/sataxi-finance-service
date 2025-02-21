from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.db.sqlalchemy.db_Language import (
    DB_LanguageInsert,
    DB_LanguageSelectAll,
    DB_LanguageSelectByDescription,
    DB_LanguageSelectOne,
    DB_LanguageUpdate,
)


def get_all_languages(session: Session) -> List[DB_LanguageSelectAll]:
    return DB_LanguageSelectAll.execute(session)


def get_language_by_description(
    session: Session, description: str
) -> DB_LanguageSelectByDescription:
    return DB_LanguageSelectByDescription.execute(session, description)


def get_language_by_id(session: Session, language_id: int):
    return DB_LanguageSelectOne.execute(session, language_id)


def insert_language(session: Session, description: str):
    return DB_LanguageInsert.execute(session, description)


def update_language(session: Session, description: str, language_id: int):
    return DB_LanguageUpdate.execute(session, description, language_id)


def delete_language_by_language_id(session: Session, language_id: int):
    return DB_LanguageSelectByDescription.execute(session, language_id)
