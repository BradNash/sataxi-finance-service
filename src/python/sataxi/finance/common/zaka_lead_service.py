from sqlalchemy.orm import Session

from sataxi.finance.common.schemas.zaka_schema import ZakaLeadDetails
from sataxi.finance.db.sqlalchemy.db_VG_Leads_ABL import DB_VG_Leads_ABLSelectOne


def get_zaka_leads_detail_by_id(session: Session, id_number: str) -> ZakaLeadDetails:
    response = DB_VG_Leads_ABLSelectOne.execute(session, id_number)

    return ZakaLeadDetails(
        response.name.strip(),
        response.ContactDetails,
        response.engineNumber,
        response.ChassisNumber,
        response.Model,
        response.Make,
        response.MakeDesc,
        response.AssetDescription,
        response.YearOfManufature,
        response.SettledDealNumber,
        response.StatusColumn,
        response.CreatedDate,
        response.DateAddedToLMS,
        response.Campaign,
        response.typeOfSale,
        response.TripsPerDay,
        response.kmPerTrip,
        response.SeatNumber,
        response.insuranceBroker,
        response.supplier,
        response.insuranceAmount,
        response.customerFirstName.strip(),
        response.customerSurname.strip(),
        response.routeFromTo,
        response.taxiAssociation,
        response.residentialDetails,
        response.Province,
        response.AccountStatus,
        response.settlement_amount,
        response.outstanding_balance,
        response.cash_payout,
    )
