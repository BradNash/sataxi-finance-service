from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.db.sqlalchemy.db_Relation import (
    DB_RelationDeleteOne,
    DB_RelationInsert,
    DB_RelationSelectAll,
    DB_RelationSelectByRelative,
    DB_RelationSelectOne,
    DB_RelationUpdate,
)


def get_all_relations(session: Session) -> List[DB_RelationSelectAll]:
    return DB_RelationSelectAll.execute(session)


def get_relation_by_relative(
    session: Session, relative: str
) -> DB_RelationSelectByRelative:
    return DB_RelationSelectByRelative.execute(session, relative)


def get_relation_by_id(session: Session, relative_id: str):
    return DB_RelationSelectOne.execute(session, relative_id)


def insert_relation(session: Session, relative: str):
    return DB_RelationInsert.execute(session, relative)


def update_relation(session: Session, relative: str, relative_id: int):
    return DB_RelationUpdate.execute(session, relative, relative_id)


def delete_relation_by_id(session: Session, relative_id: int):
    return DB_RelationDeleteOne.execute(session, relative_id)
