from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.db.sqlalchemy.db_EmployerIndustryType import (
    DB_EmployerIndustryTypeDeleteOne,
    DB_EmployerIndustryTypeInsert,
    DB_EmployerIndustryTypeSelectAll,
    DB_EmployerIndustryTypeSelectByType,
    DB_EmployerIndustryTypeSelectOne,
    DB_EmployerIndustryTypeUpdate,
)


def get_all_employer_industry_types(
    session: Session,
) -> List[DB_EmployerIndustryTypeSelectAll]:
    return DB_EmployerIndustryTypeSelectAll.execute(session)


def get_employer_industry_type_by_type(
    session: Session, type: str
) -> DB_EmployerIndustryTypeSelectByType:
    return DB_EmployerIndustryTypeSelectByType.execute(session, type)


def get_employer_industry_type_by_id(session: Session, industry_type_id: int):
    return DB_EmployerIndustryTypeSelectOne.execute(session, industry_type_id)


def insert_employer_industry_type(session: Session, type: str):
    return DB_EmployerIndustryTypeInsert.execute(session, type)


def update_employer_industry_type(session: Session, type: str, industry_type_id: int):
    return DB_EmployerIndustryTypeUpdate.execute(session, type, industry_type_id)


def delete_employer_industry_type_by_id(session: Session, industry_type_id: int):
    return DB_EmployerIndustryTypeDeleteOne.execute(session, industry_type_id)
