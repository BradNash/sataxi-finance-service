import logging
from datetime import datetime

from bbdcommon.pybus.common_types import SagaBase
from bbdcommon.pybus.handler_register_functions import (
    HandleRegister,
    HandleFuncRegister,
)
from bbdcommon.pybus.service_bus import KombuBus

from sataxi.finance.db.sqlalchemy import DB_VG_Leads_ABLUpdateZakaLead
from sataxi.finance.messaging.events.zaka_case_created import ZakaCaseCreatedV1


@HandleRegister()
class EventSaga(SagaBase):
    def __init__(self, bus: KombuBus = None):
        super(EventSaga, self).__init__(bus)
        self.session = self.bus_ref.db_registry["MSG"].get_session()

    @HandleFuncRegister(ZakaCaseCreatedV1)
    def zaka_case_created_event_handler(self, msg: ZakaCaseCreatedV1):
        with self.bus_ref.db_registry["HiveRepository"].get_session() as hive_session:
            logging.debug(f"Processing Message {msg.__dict__}")
            try:
                DB_VG_Leads_ABLUpdateZakaLead.execute(
                    hive_session,
                    msg.id_number,
                    msg.engine_number,
                    msg.campaign,
                    datetime.now(),
                )
                hive_session.commit()
            except Exception as e:
                logging.error(e)
                logging.error(
                    f"Updating Lead Failed --> Case Number: {msg.case_no}, IDNumber: {msg.id_number},"
                    f"engineNumber: {msg.engine_number}, Campaign {msg.campaign}"
                )

        logging.debug(f"Zaka lead updated, Case created {msg.case_no}")
