from dataclasses import dataclass
from datetime import datetime

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class ZakaLeadDetails:
    name: str = schema_field(data_key="name", required=True)
    contact_details: str = schema_field(data_key="ContactDetails", required=True)
    engine_number: str = schema_field(data_key="engineNumber", required=True)
    chassis_number: str = schema_field(data_key="ChassisNumber")
    model: str = schema_field(data_key="Model", required=True)
    make: str = schema_field(data_key="Make", required=True)
    make_desc: str = schema_field(data_key="MakeDesc", required=True)
    asset_description: str = schema_field(data_key="AssetDescription", required=True)
    year_of_manufature: int = schema_field(data_key="YearOfManufature", required=True)
    settled_deal_number: str = schema_field(data_key="SettledDealNumber", required=True)
    status_column: int = schema_field(data_key="StatusColumn", required=True)
    created_Date: datetime = schema_field(data_key="CreatedDate", required=True)
    date_added_to_lms: datetime = schema_field(data_key="DateAddedToLMS", required=True)
    campaign: str = schema_field(data_key="Campaign", required=True)
    type_of_sale: str = schema_field(data_key="typeOfSale", required=True)
    trips_per_day: int = schema_field(data_key="TripsPerDay", required=True)
    km_per_trip: float = schema_field(data_key="kmPerTrip", required=True)
    seat_number: str = schema_field(data_key="SeatNumber", required=True)
    insurance_broker: str = schema_field(data_key="insuranceBroker", required=True)
    supplier: str = schema_field(data_key="supplier", required=True)
    insurance_amount: float = schema_field(data_key="insuranceAmount", required=True)
    customer_first_name: str = schema_field(data_key="customerFirstName", required=True)
    customer_surname: str = schema_field(data_key="customerSurname", required=True)
    route_from_to: str = schema_field(data_key="routeFromTo", required=True)
    taxi_association: str = schema_field(data_key="taxiAssociation", required=True)
    residential_details: str = schema_field(
        data_key="residentialDetails", required=True
    )
    province: str = schema_field(data_key="Province", required=True)
    account_status: str = schema_field(data_key="AccountStatus", required=True)
    settlement_amount: float = schema_field(data_key="settlement_amount", required=True)
    outstanding_balance: float = schema_field(
        data_key="outstanding_balance", required=True
    )
    cash_payout: float = schema_field(data_key="cash_payout", required=True)
