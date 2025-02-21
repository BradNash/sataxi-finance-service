import asyncio
import logging
from datetime import datetime
from enum import IntEnum
from typing import List

from bbdcommon.pybus.py_node import PyNode

from sataxi.finance.db.sqlalchemy import DB_VG_Leads_ABLSelectPendingLeads
from sataxi.finance.messaging.commands.create_zaka_case import (
    ZakaCreateCaseV1,
    CaseReferenceSecondry,
    ProcessData,
)

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("batch_node")

ZAKA_PROC_SYSID = 10002
ZAKA_DATA_SYSID = 22211113


class ReferenceTypes(IntEnum):
    ID_NUMBER = 1
    ENGINE_NUMBER = 2
    CAMPAIGN = 3
    CONTACT_NUMBER = 4


class CreateLeadCasesNode(PyNode):
    def create_case_request(self, lead: DB_VG_Leads_ABLSelectPendingLeads) -> int:
        process_data_dict = {
            "IdNumber": lead.IDNumber.strip() or "",
            "EngineNumber": lead.engineNumber.strip() or "",
            "Campaign": lead.Campaign.strip() or ""
            # "FullName": lead.name.strip() or "",
            # "ContactDetails": lead.ContactDetails.strip() or "",
            # "VehicleModel": lead.Model.strip() or "",
            # "VehicleMake": lead.Make.strip() or "",
            # "YearOfManufature": int(lead.YearOfManufature) if lead.YearOfManufature else -1,
            # "CreatedDate": lead.CreatedDate.strftime("%Y-%m-%d") if lead.CreatedDate else "",
            # "TaxiAssociation": lead.taxiAssociation.strip() or ""
        }
        process_data: List[ProcessData] = [
            ProcessData(ZAKA_DATA_SYSID, process_data_dict)
        ]

        additional_references: List[CaseReferenceSecondry] = []
        additional_references.append(
            CaseReferenceSecondry(
                ReferenceTypes.CONTACT_NUMBER.value, lead.ContactDetails
            )
        )
        additional_references.append(
            CaseReferenceSecondry(
                ReferenceTypes.ENGINE_NUMBER.value, lead.engineNumber.strip()
            )
        )
        additional_references.append(
            CaseReferenceSecondry(ReferenceTypes.CAMPAIGN.value, lead.Campaign.strip())
        )

        create_zaka_case = ZakaCreateCaseV1(
            process_type_sysid=ZAKA_PROC_SYSID,
            reference_type=ReferenceTypes.ID_NUMBER.value,
            reference=lead.IDNumber,
            reference_year=lead.CreatedDate.year,
            # reference_year=2009,
            area_code="",
            status="Case created",
            channel="",
            title="Zaka Lead case",
            process_data=process_data,
            process_data_extensions=[],
            additional_references=additional_references,
            id_number=lead.IDNumber.strip(),
            engine_number=lead.engineNumber.strip(),
            campaign=lead.Campaign.strip(),
            user=r"sp\batch_user",
        )

        self.bus.send(msg_obj=create_zaka_case, reply_node_id="ZAKA_CASE_CREATED_V1")
        self.bus.commit_messaging()
        self.bus.emit_prompts()
        self.bus.reset_state()

    async def create_cases(self):
        zaka_hive_leads: List[DB_VG_Leads_ABLSelectPendingLeads] = []
        with self.database_registry["HiveRepository"].get_session() as hive_session:
            zaka_hive_leads = DB_VG_Leads_ABLSelectPendingLeads.execute(hive_session, 0)

        for lead in zaka_hive_leads:
            self.create_case_request(lead)

        logger.debug(f"{len(zaka_hive_leads)} number of cases created")
        logger.debug("Batch Completed!")


async def main_func():
    logger.debug("CreateLeadCasesNode main")
    logger.debug(f"--- Batch starting {datetime.now()} ---")
    node = CreateLeadCasesNode()
    asyncio.get_event_loop().create_task(node.create_cases())
    pending = asyncio.all_tasks()
    pending.remove(asyncio.current_task())
    logger.debug(f"--- Batch Completed {datetime.now()} ---")
    await asyncio.gather(*pending)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_func())


if __name__ == "__main__":
    main()
