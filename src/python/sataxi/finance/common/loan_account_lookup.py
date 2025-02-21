from typing import List

from sqlalchemy.orm import Session

from sataxi.finance.common.schemas.collect_smart_schema import (
    CollectSmartClientDetailsResponse,
)
from sataxi.finance.common.schemas.loan_schema import (
    LoanAccountLookupResponse,
    LoanDetailsLookupResponse,
)
from sataxi.finance.common.schemas.vg_details_loan_gomo import VGDetailsLoanGomoResponse
from sataxi.finance.common.schemas.vg_validation_loan_gomo import (
    VGValidationLoanGomoResponse,
)
from sataxi.finance.db.sqlalchemy.db_VG_Details_Loan import (
    DB_VG_Details_LoanSelectClientDetails,
)
from sataxi.finance.db.sqlalchemy.db_VG_Details_Loan_Gomo import (
    DB_VG_Details_Loan_GomoSelectByAccountNumber,
)
from sataxi.finance.db.sqlalchemy.db_VG_Validation_Loan import (
    DB_VG_Validation_LoanSelectAccountByID,
    DB_VG_Validation_LoanSelectAccountByAccountNumber,
    DB_VG_Validation_LoanSelectLoanDetails,
)
from sataxi.finance.db.sqlalchemy.db_VG_Validation_Loan_Gomo import (
    DB_VG_Validation_Loan_GomoSelectByAccountNumber,
    DB_VG_Validation_Loan_GomoSelectByIDNumber,
)


def check_identifier(account_number="", id_no="") -> bool:
    use_account_number: bool = False

    if (
        id_no is not None
        and account_number is not None
        and id_no != ""
        and account_number != ""
    ):
        use_account_number = True

    if account_number is not None and account_number != "":
        use_account_number = True

    if id_no is not None and id_no != "":
        use_account_number = False

    return use_account_number


def get_loan_accounts(session: Session, account_number: str, id_number: str):
    use_account_number = check_identifier(
        account_number=account_number, id_no=id_number
    )
    if use_account_number:
        loan_accounts = DB_VG_Validation_LoanSelectAccountByAccountNumber.execute(
            session, account_number
        )
    else:
        loan_accounts = DB_VG_Validation_LoanSelectAccountByID.execute(
            session, id_number
        )

    loan_account_list: List[LoanAccountLookupResponse] = []
    for loan_account in loan_accounts:
        loan_account_list.append(
            LoanAccountLookupResponse(
                loan_account.AccountNumber,
                loan_account.IDNo,
                loan_account.CustomerName,
                loan_account.Mobile,
                loan_account.TaxiAssociation,
                loan_account.ResidentialAddress,
                loan_account.PostalAddress,
                loan_account.NextInstalmentDate,
                loan_account.InstalmentDay,
                loan_account.PaymentType,
                loan_account.LoanStartDate,
                loan_account.BankAccountNumber,
                loan_account.BankAccountType,
                loan_account.BankName,
                loan_account.AccountStatus,
                loan_account.TotalDueCS,
                loan_account.EmailAddress,
            )
        )
    return loan_account_list


def get_loan_details(session: Session, account_number: str):
    loan_details = DB_VG_Validation_LoanSelectLoanDetails.execute(
        session, account_number
    )

    loan_detailst_list: List[LoanDetailsLookupResponse] = []

    for loan_detail in loan_details:
        loan_detailst_list.append(
            LoanDetailsLookupResponse(
                loan_detail.AccountNumber,
                loan_detail.InstalmentDay,
                loan_detail.AccountStatus,
                loan_detail.LoanStartDate,
                loan_detail.PaymentMethod,
                loan_detail.AccountHolder,
                loan_detail.BankAccountNumber,
                loan_detail.BankAccountType,
                loan_detail.BankName,
                loan_detail.VehicleDescription,
                loan_detail.TotalDueCS,
                loan_detail.DeviceHealth,
                loan_detail.CarTrackSignalDate,
                loan_detail.Capital,
                loan_detail.OutstandingBalance,
                loan_detail.InstallmentAmount,
                loan_detail.NextInstallmentAmount,
                loan_detail.NextInstalmentDate,
                loan_detail.LegalFeeBalance,
                loan_detail.DealExpiryDate,
                loan_detail.LoanAccruedInt,
                loan_detail.TotalReceivable,
                loan_detail.InterestRate,
                loan_detail.InitialTerm,
                loan_detail.InstalmentsRemaining,
                loan_detail.MonthsInArrears,
                loan_detail.DealExpiryDateWithArrears,
                loan_detail.SettlementDate,
                loan_detail.ChassisNumber,
                loan_detail.EngineNumber,
                loan_detail.YearOfManufacture,
                loan_detail.RegistrationNumber,
                loan_detail.FirstInstalmentDate,
                loan_detail.Product,
                loan_detail.EasyPay,
                loan_detail.Source,
                loan_detail.FieldAgent,
                loan_detail.FieldAgentInstruction,
                loan_detail.CompanyName,
                loan_detail.NCRRegNo,
                loan_detail.PreviousCompanyName,
            )
        )
    return loan_detailst_list


def get_collect_smart_client_details(session: Session, account_number: str):
    collect_smart_details = DB_VG_Details_LoanSelectClientDetails.execute(
        session, account_number
    )

    if collect_smart_details is None:
        return None

    return CollectSmartClientDetailsResponse(
        collect_smart_details.AccountNumber,
        collect_smart_details.AccountHolder,
        collect_smart_details.AccountStatus,
        collect_smart_details.VehicleDescription,
        collect_smart_details.TotalDueCS,
        collect_smart_details.DeviceHealth,
        collect_smart_details.CarTrackSignalDate,
        collect_smart_details.Capital,
        collect_smart_details.OutstandingBalance,
        collect_smart_details.InstallmentAmount,
        collect_smart_details.NextInstallmentAmount,
        collect_smart_details.LegalFeeBalance,
        collect_smart_details.DealExpiryDate,
        collect_smart_details.LoanAccruedInt,
        collect_smart_details.TotalReceivable,
        collect_smart_details.InterestRate,
        collect_smart_details.InitialTerm,
        collect_smart_details.InstalmentsRemaining,
        collect_smart_details.MonthsInArrears,
        collect_smart_details.DealExpiryDateWithArrears,
        collect_smart_details.SettlementDate,
        collect_smart_details.ChassisNumber,
        collect_smart_details.EngineNumber,
        collect_smart_details.YearOfManufacture,
        collect_smart_details.RegistrationNumber,
        collect_smart_details.FirstInstalmentDate,
        collect_smart_details.Product,
        collect_smart_details.EasyPay,
        collect_smart_details.Agent,
        collect_smart_details.Supervisor,
        collect_smart_details.PaymentMTD,
        collect_smart_details.ArrearsAccruedInt,
        collect_smart_details.Short_Over,
        collect_smart_details.SecondaryStatus,
        collect_smart_details.LastPaymentDate,
        collect_smart_details.LastPaymentAmount,
        collect_smart_details.PendingActivity,
        collect_smart_details.LegalAdministrator,
        collect_smart_details.Attorney,
        collect_smart_details.HandoverDate,
        collect_smart_details.ArrearsAmountAtHO,
        collect_smart_details.LSCaseNumber,
        collect_smart_details.SummonsIssueDate,
        collect_smart_details.SummonsServedDate,
        collect_smart_details.DateOfJudgement,
        collect_smart_details.WarrantIssuedDate,
        collect_smart_details.Source,
        collect_smart_details.FieldAgent,
        collect_smart_details.FieldAgentInstruction,
    )


def get_gomo_loan_accounts(session: Session, account_number: str):
    # TODO: Currently done manually, would be better to do with a class_schema(...).dump()
    loan_accounts = DB_VG_Details_Loan_GomoSelectByAccountNumber.execute(
        session, account_number
    )
    loan_account_list: List[VGDetailsLoanGomoResponse] = []
    for account in loan_accounts:
        loan_account = VGDetailsLoanGomoResponse(
            # Note: Rounding Money values to remove floating point errors in DB values.
            # If else required to catch if value is Null in DB
            account.AccountHolder,
            account.AccountNumber,
            account.AccountStatus,
            round(account.ArrearsAccruedInt, 2)
            if account.ArrearsAccruedInt is not None
            else account.ArrearsAccruedInt,
            account.BankAccountNumber,
            account.BankAccountType,
            account.BankName,
            round(account.Capital, 2)
            if account.Capital is not None
            else account.Capital,
            account.chassisnumber,
            account.DealExpiryDate,
            account.DealExpiryDateWithArrears,
            account.EasyPay,
            account.enginenumber,
            account.FirstInstalmentDate,
            account.initialterm,
            round(account.InstallmentAmount, 2)
            if account.InstallmentAmount is not None
            else account.InstallmentAmount,
            account.InstalmentDay,
            account.InstalmentsRemaining,
            account.Interestrate,
            round(account.LegalFeeBalance, 2)
            if account.LegalFeeBalance is not None
            else account.LegalFeeBalance,
            account.LoanAccruedInt,
            account.LoanStartDate,
            account.MMCode,
            account.MonthsInArrears,
            round(account.NextInstallmentAmount, 2)
            if account.NextInstallmentAmount is not None
            else account.NextInstallmentAmount,
            round(account.OutstandingBalance, 2)
            if account.OutstandingBalance is not None
            else account.OutstandingBalance,
            account.PaymentMethod,
            account.Product,
            account.registrationnumber,
            account.SecondaryStatus,
            account.settlementdate,
            account.SupplierName,
            round(account.TotalDueCS, 2)
            if account.TotalDueCS is not None
            else account.TotalDueCS,
            round(account.TotalReceivable, 2)
            if account.TotalReceivable is not None
            else account.TotalReceivable,
            account.VehicleDescription,
            account.YearOfManufature,
            account.StructureCode
        )
        loan_account_list.append(loan_account)
    return loan_account_list


def get_gomo_validation_loan_accounts(
    session: Session, id_no: str = "", account_number: str = ""
):
    use_account_number = check_identifier(account_number=account_number, id_no=id_no)
    if use_account_number:
        validation_loan_accounts = (
            DB_VG_Validation_Loan_GomoSelectByAccountNumber.execute(
                session, account_number
            )
        )
    else:
        validation_loan_accounts = DB_VG_Validation_Loan_GomoSelectByIDNumber.execute(
            session, id_no
        )

    validation_loan_list: List[VGValidationLoanGomoResponse] = []

    for validation_account in validation_loan_accounts:
        validation_loan_list.append(
            VGValidationLoanGomoResponse(
                # Note: Rounding Money values to remove floating point errors in DB values.
                # If else required to catch if value is Null in DB
                validation_account.AccountNumber,
                validation_account.IDNo,
                validation_account.CustomerName,
                validation_account.Mobile,
                validation_account.PhysicalAddress,
                validation_account.PostalAddress,
                validation_account.NextInstalmentDate,
                validation_account.InstalmentDay,
                validation_account.PaymentType,
                validation_account.LoanStartDate,
                validation_account.BankAccountNumber,
                validation_account.BankAccountType,
                validation_account.BankName,
                validation_account.AccountStatus,
                validation_account.EmailAddress,
                round(validation_account.TotalDueCS, 2)
                if validation_account.TotalDueCS is not None
                else validation_account.TotalDueCS,
                validation_account.StructureCode
            )
        )
    return validation_loan_list
