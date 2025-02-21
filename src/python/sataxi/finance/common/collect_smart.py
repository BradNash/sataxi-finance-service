from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.common.schemas.collect_smart_schema import (
    PTPDetailsResponse,
    CampaignDetailsResponse,
)
from sataxi.finance.db.sqlalchemy.db_CollectSmart_View_GetPTPDetails import (
    DB_CollectSmart_View_GetPTPDetailsSelectPTPDetails,
)
from sataxi.finance.db.sqlalchemy.db_VG_View_LoanNoteDetails import (
    DB_VG_View_LoanNoteDetailsSelectNoteByAccountNumber,
)


def get_ptp_details(session: Session, account_number: str):
    details = DB_CollectSmart_View_GetPTPDetailsSelectPTPDetails.execute(
        session, account_number
    )
    ptp_details: List[PTPDetailsResponse] = []
    for ptp in details:
        ptp_details.append(
            PTPDetailsResponse(
                account_number=ptp.AccountNumber,
                agent_id=ptp.AgentID,
                campaign_date=ptp.CampaignDate,
                campaign_id=ptp.CampaignID,
                campaign_name=ptp.CampaignName,
                client_id=ptp.ClientID,
                current_payment=ptp.CurrentPayment,
                frequency=ptp.Frequency,
                name=ptp.Name,
                ptp_amount=ptp.PTPAmount,
                ptp_created_date=ptp.PTPCreatedDate,
                ptp_date=ptp.PTPDate,
                ptpid=ptp.PTPID,
                ptp_status=ptp.PTPStatus,
                ptp_type=ptp.PTPType,
                user_name=ptp.UserName,
            )
        )

    return ptp_details


def get_campaign_details(session: Session, account_number: str):
    details = DB_VG_View_LoanNoteDetailsSelectNoteByAccountNumber.execute(
        session, account_number
    )

    campaigns: List[CampaignDetailsResponse] = []

    for campaign in details:
        campaigns.append(
            CampaignDetailsResponse(
                note_text=campaign.NoteText,
                note_category=campaign.NoteCategory,
                username=campaign.UserName,
                note_system=campaign.NoteSystem,
                created_date=campaign.CreatedDate,
            )
        )
    return campaigns
