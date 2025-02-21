from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.db.sqlalchemy.db_Agreement import (
    DB_AgreementDeleteOne,
    DB_AgreementInsert,
    DB_AgreementSelectAll,
    DB_AgreementSelectByDescription,
    DB_AgreementSelectOne,
    DB_AgreementUpdate,
)


def get_all_agreements(session: Session) -> List[DB_AgreementSelectAll]:
    return DB_AgreementSelectAll.execute(session)


def get_agreement_by_description(
    session: Session, description: str
) -> DB_AgreementSelectByDescription:
    return DB_AgreementSelectByDescription.execute(session, description)


def get_agreement_by_id(session: Session, agreement_id: int):
    return DB_AgreementSelectOne.execute(session, agreement_id)


def insert_agreement(session: Session, description: str):
    return DB_AgreementInsert.execute(session, description)


def update_agreement(session: Session, agreement: str, agreement_id: int):
    return DB_AgreementUpdate.execute(session, agreement, agreement_id)


def delete_agreement_by_id(session: Session, agreement_id: int):
    return DB_AgreementDeleteOne.execute(session, agreement_id)
