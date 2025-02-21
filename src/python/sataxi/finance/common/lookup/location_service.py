from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.db.sqlalchemy.db_Area import (
    DB_AreaDeleteOne,
    DB_AreaInsert,
    DB_AreaSelectAll,
    DB_AreaSelectByAreaName,
    DB_AreaSelectOne,
    DB_AreaUpdate,
)
from sataxi.finance.db.sqlalchemy.db_Country import (
    DB_CountryDeleteOne,
    DB_CountryInsert,
    DB_CountrySelectAll,
    DB_CountrySelectByCountryName,
    DB_CountrySelectOne,
    DB_CountryUpdate,
)


def get_all_areas(session: Session) -> List[DB_AreaSelectAll]:
    return DB_AreaSelectAll.execute(session)


def get_area_by_name(session: Session, area_name: str) -> DB_AreaSelectByAreaName:
    return DB_AreaSelectByAreaName.execute(session, area_name)


def get_area_by_id(session: Session, area_id: int):
    return DB_AreaSelectOne.execute(session, area_id)


def insert_area(session: Session, area_name: str):
    return DB_AreaInsert.execute(session, area_name)


def update_area(session: Session, area_name: str, area_id: int):
    return DB_AreaUpdate.execute(session, area_name, area_id)


def delete_area(session: Session, area_id: int):
    return DB_AreaDeleteOne.execute(session, area_id)


def get_all_countries(session: Session) -> List[DB_CountrySelectAll]:
    return DB_CountrySelectAll.execute(session)


def get_country_by_name(
    session: Session, country_name: str
) -> DB_CountrySelectByCountryName:
    return DB_CountrySelectByCountryName.execute(session, country_name)


def get_country_by_id(session: Session, country_id: int):
    return DB_CountrySelectOne.execute(session, country_id)


def insert_country(session: Session, country_name: str):
    return DB_CountryInsert.execute(session, country_name)


def update_country(session: Session, country_name: str, country_id: int):
    return DB_CountryUpdate.execute(session, country_name, country_id)


def delete_country(session: Session, country_id: int):
    return DB_CountryDeleteOne.execute(session, country_id)
