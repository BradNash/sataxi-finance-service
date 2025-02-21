from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.db.sqlalchemy.db_Occupation import (
    DB_OccupationDeleteOne,
    DB_OccupationInsert,
    DB_OccupationSelectAll,
    DB_OccupationSelectByOccupation,
    DB_OccupationSelectOne,
    DB_OccupationUpdate,
)


def get_all_occupations(session: Session) -> List[DB_OccupationSelectAll]:
    return DB_OccupationSelectAll.execute(session)


def get_occupation_by_occupation(
    session: Session, occupation: str
) -> DB_OccupationSelectByOccupation:
    return DB_OccupationSelectByOccupation.execute(session, occupation)


def get_occupation_by_id(session: Session, occupation_id: int):
    return DB_OccupationSelectOne.execute(session, occupation_id)


def insert_occupation(session: Session, occupation: str):
    return DB_OccupationInsert.execute(session, occupation)


def update_occupation(session: Session, occupation: str, occupation_id: int):
    return DB_OccupationUpdate.execute(session, occupation, occupation_id)


def delete_occupation_by_id(session: Session, occupation_id: int):
    return DB_OccupationDeleteOne.execute(session, occupation_id)
