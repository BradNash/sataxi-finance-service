from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.db.sqlalchemy.db_InsuranceBroker import (
    DB_InsuranceBrokerDeleteOne,
    DB_InsuranceBrokerInsert,
    DB_InsuranceBrokerSelectAll,
    DB_InsuranceBrokerSelectByBrokerName,
    DB_InsuranceBrokerSelectOne,
    DB_InsuranceBrokerUpdate,
)
from sataxi.finance.db.sqlalchemy.db_InsuranceCompany import (
    DB_InsuranceCompanyDeleteOne,
    DB_InsuranceCompanyInsert,
    DB_InsuranceCompanySelectAll,
    DB_InsuranceCompanySelectByCompanyName,
    DB_InsuranceCompanySelectOne,
    DB_InsuranceCompanyUpdate,
)


def get_all_insurance_companies(session: Session) -> List[DB_InsuranceCompanySelectAll]:
    return DB_InsuranceCompanySelectAll.execute(session)


def get_insurance_company_by_name(
    session: Session, company_name: str
) -> DB_InsuranceCompanySelectByCompanyName:
    return DB_InsuranceCompanySelectByCompanyName.execute(session, company_name)


def get_insurance_company_by_id(session: Session, company_id: int):
    return DB_InsuranceCompanySelectOne.execute(session, company_id)


def insert_insurance_company(session: Session, company_name: str):
    return DB_InsuranceCompanyInsert.execute(session, company_name)


def update_insurance_company(session: Session, company_name: str, company_id: int):
    return DB_InsuranceCompanyUpdate.execute(session, company_name, company_id)


def delete_insurance_company_by_id(session: Session, company_id: int):
    return DB_InsuranceCompanyDeleteOne.execute(session, company_id)


def get_all_insurance_brokers(session: Session) -> List[DB_InsuranceBrokerSelectAll]:
    return DB_InsuranceBrokerSelectAll.execute(session)


def get_insurance_broker_by_name(
    session: Session, broker_name: str
) -> DB_InsuranceBrokerSelectByBrokerName:
    return DB_InsuranceBrokerSelectByBrokerName.execute(session, broker_name)


def get_insurance_broker_by_id(session: Session, broker_id: int):
    return DB_InsuranceBrokerSelectOne.execute(session, broker_id)


def insert_insurance_broker(session: Session, broker_name: str):
    return DB_InsuranceBrokerInsert.execute(session, broker_name)


def update_insurance_broker(session: Session, broker_name: str, broker_id: int):
    return DB_InsuranceBrokerUpdate.execute(session, broker_name, broker_id)


def delete_insurance_broker_by_id(session: Session, broker_id: int):
    return DB_InsuranceBrokerDeleteOne.execute(session, broker_id)
