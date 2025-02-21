import json
from dataclasses import dataclass
from enum import IntEnum

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class Campaign(IntEnum):
    ZAKA = 0
    TRADE_UP = 1


@dataclass
class Application:
    customerIdType: str = schema_field(
        data_key="customerIdType", required=False, default=""
    )
    customerSurname: str = schema_field(
        data_key="customerSurname", required=False, default=""
    )
    isSataxiFinance: str = schema_field(
        data_key="sataxiFinance", required=False, default="No"
    )
    thirdPartyEmail: str = schema_field(
        data_key="thirdPartyEmail", required=False, default=""
    )
    customerIdNumber: str = schema_field(
        data_key="customerIdNumber", required=False, default=""
    )
    customerFirstName: str = schema_field(
        data_key="customerFirstName", required=False, default=""
    )
    customerIdVerified: str = schema_field(
        data_key="customerIdVerified", required=False, default="No"
    )
    customerMiddleName: str = schema_field(
        data_key="customerMiddleName", required=False, default=""
    )
    customerDateOfBirth: str = schema_field(
        data_key="customerDateOfBirth", required=False, default="1900-01-01 00:00:00"
    )
    advertisementReference: str = schema_field(
        data_key="advertisementReference", required=False, default=""
    )
    customerDriversLicenseVerified: str = schema_field(
        data_key="customerDriversLicenseVerified", required=False, default="No"
    )
    typeOfSale: str = schema_field(data_key="typeOfSale", required=False, default="")
    dealerCode: str = schema_field(data_key="dealerCode", required=False, default="")


@dataclass
class VehicleDetails:
    articleType: str = schema_field(
        data_key="articleType", required=False, default="Motor Vehicle"
    )
    articleCondition: str = schema_field(
        data_key="articleCondition", required=False, default=""
    )
    articleUse: str = schema_field(data_key="articleUse", required=False, default="")
    yearOfFirstRegistration: int = schema_field(
        data_key="yearOfFirstRegistration", required=False, default=0
    )
    make: str = schema_field(data_key="make", required=False, default="")
    vehicleDescription: str = schema_field(
        data_key="vehicleDescription", required=False, default=""
    )
    mmCode: str = schema_field(data_key="mmCode", required=False, default="")
    retailValue: float = schema_field(
        data_key="retailValue", required=False, default=0.00
    )
    purchasePriceIncludingVat: float = schema_field(
        data_key="purchasePriceIncludingVat", required=False, default=0.00
    )
    kilometerReading: float = schema_field(
        data_key="kilometerReading", required=False, default=0.00
    )
    articleColour: str = schema_field(
        data_key="articleColour", required=False, default=""
    )
    kilometerCategory: str = schema_field(
        data_key="kilometerCategory", required=False, default=""
    )
    chassisNo: str = schema_field(data_key="chassisNo", required=False, default="")
    registrationNumber: str = schema_field(
        data_key="registrationNumber", required=False, default=""
    )
    engineNumber: str = schema_field(
        data_key="engineNumber", required=False, default=""
    )
    serialNumber: str = schema_field(
        data_key="serialNumber", required=False, default=""
    )
    stockNumber: str = schema_field(data_key="stockNumber", required=False, default="")
    vehicleEngineSize: int = schema_field(
        data_key="vehicleEngineSize", required=False, default=0
    )
    vehicleNumberOfSeats: int = schema_field(
        data_key="vehicleNumberOfSeats", required=False, default="0"
    )
    regtrackIndicatorTag: str = schema_field(
        data_key="regtrackIndicatorTag", required=False, default="No"
    )
    isFinanceTrackUnit: str = schema_field(
        data_key="isFinanceTrackUnit", required=False, default="No"
    )
    vehicleType: str = schema_field(
        data_key="vehicleType", required=False, default="New/Repossessed"
    )


@dataclass
class FinanceDetails:
    agreementType: str = schema_field(
        data_key="agreementType", required=False, default=""
    )
    repaymentPeriod: str = schema_field(
        data_key="repaymentPeriod", required=False, default=""
    )
    purchasePrice: float = schema_field(
        data_key="purchasePrice", required=False, default=0.00
    )
    deposit: float = schema_field(data_key="deposit", required=False, default=0.00)
    paymentFrequency: str = schema_field(
        data_key="paymentFrequency", required=False, default=""
    )
    interestRate: float = schema_field(
        data_key="interestRate", required=False, default=0.00
    )
    rateIndicator: str = schema_field(
        data_key="rateIndicator", required=False, default=""
    )
    residualValue: float = schema_field(
        data_key="residualValue", required=False, default=0.00
    )
    dealType: str = schema_field(data_key="dealType", required=False, default="")
    schemeCodeWesbank: int = schema_field(
        data_key="schemeCodeWesbank", required=False, default=0
    )
    schemeCodeMFC: int = schema_field(
        data_key="schemeCodeMFC", required=False, default=0
    )
    sourceOfDeposit: str = schema_field(
        data_key="sourceOfDeposit", required=False, default=""
    )
    financeInitiationFees: str = schema_field(
        data_key="financeInitiationFees", required=False, default="Yes"
    )
    advance: str = schema_field(data_key="advance", required=False, default="No")
    takeABreakMonth: str = schema_field(
        data_key="takeABreakMonth", required=False, default=""
    )
    shockAbsorberWesbank: str = schema_field(
        data_key="shockAbsorberWesbank", required=False, default="No"
    )
    TCMIndicator: str = schema_field(
        data_key="TCMIndicator", required=False, default="No"
    )
    newRate: int = schema_field(data_key="newRate", required=False, default=0)


@dataclass
class PersonalDetails:
    customerPreferredLanguage: str = schema_field(
        data_key="customerPreferredLanguage", required=False, default=""
    )
    customerGender: str = schema_field(
        data_key="customerGender", required=False, default=""
    )
    customerTitle: str = schema_field(
        data_key="customerTitle", required=False, default=""
    )
    customerRaceEthnicGroup: str = schema_field(
        data_key="customerRaceEthnicGroup", required=False, default=""
    )
    customerNationality: str = schema_field(
        data_key="customerNationality", required=False, default=""
    )
    customerGraduate: str = schema_field(
        data_key="customerGraduate", required=False, default="No"
    )
    customerMaritalStatus: str = schema_field(
        data_key="customerMaritalStatus", required=False, default=""
    )
    customerMaritalContract: str = schema_field(
        data_key="customerMaritalContract", required=False, default=""
    )
    dateMarried: str = schema_field(data_key="dateMarried", required=False, default="")
    customerPreferredContactMethod: str = schema_field(
        data_key="customerPreferredContactMethod", required=False, default=""
    )
    customerMobilePhoneNumber: str = schema_field(
        data_key="customerMobilePhoneNumber", required=False, default=""
    )
    mobileType: str = schema_field(data_key="mobileType", required=False, default="")
    customerHomePhoneNumber: str = schema_field(
        data_key="customerHomePhoneNumber", required=False, default=""
    )
    customerWorkPhoneNumberType: str = schema_field(
        data_key="customerWorkPhoneNumberType", required=False, default=""
    )
    customerWorkPhoneNumber: str = schema_field(
        data_key="customerWorkPhoneNumber", required=False, default=""
    )
    customerEmail: str = schema_field(
        data_key="customerEmail", required=False, default=""
    )
    countryOfBirth: str = schema_field(
        data_key="countryOfBirth", required=False, default=""
    )
    isForeignOrTaxObligation: str = schema_field(
        data_key="isForeignOrTaxObligation", required=False, default="No"
    )
    isMultipleNationalities: str = schema_field(
        data_key="isMultipleNationalities", required=False, default="No"
    )
    wasSouthAfricanCitizen: str = schema_field(
        data_key="wasSouthAfricanCitizen", required=False, default="No"
    )
    countryCitizenship: str = schema_field(
        data_key="countryCitizenship", required=False, default=""
    )
    residentialAddressCountry: str = schema_field(
        data_key="residentialAddressCountry", required=False, default=""
    )
    mfcClientType: str = schema_field(
        data_key="mfcClientType", required=False, default=""
    )


@dataclass
class ResidentialDetails:
    customerResidentialAddressLine1: str = schema_field(
        data_key="customerResidentialAddressLine1", required=False, default=""
    )
    customerResidentialAddressLine2: str = schema_field(
        data_key="customerResidentialAddressLine2", required=False, default=""
    )
    customerResidentialAddressSuburb: str = schema_field(
        data_key="customerResidentialAddressSuburb", required=False, default=""
    )
    customerResidentialAddressCity: str = schema_field(
        data_key="customerResidentialAddressCity", required=False, default=""
    )
    customerResidentialAddressPostalCode: str = schema_field(
        data_key="customerResidentialAddressPostalCode", required=False, default=""
    )
    sameAsRes: str = schema_field(data_key="sameAsRes", required=False, default="")
    customerPostalAddressLine1: str = schema_field(
        data_key="customerPostalAddressLine1", required=False, default=""
    )
    customerPostalAddressSuburb: str = schema_field(
        data_key="customerPostalAddressSuburb", required=False, default=""
    )
    customerPostalAddressCity: str = schema_field(
        data_key="customerPostalAddressCity", required=False, default=""
    )
    customerPostalAddressPostalCode: str = schema_field(
        data_key="customerPostalAddressPostalCode", required=False, default=""
    )
    ownerTenantLodger: str = schema_field(
        data_key="ownerTenantLodger", required=False, default=""
    )
    outstandingBondBalance: float = schema_field(
        data_key="outstandingBondBalance", required=False, default=0.00
    )
    jointHomeloanIndicator: str = schema_field(
        data_key="jointHomeloanIndicator", required=False, default="No"
    )
    jointBondPercentage: str = schema_field(
        data_key="jointBondPercentage", required=False, default=""
    )
    residentialOwner: str = schema_field(
        data_key="residentialOwner", required=False, default=""
    )
    facilityValue: float = schema_field(
        data_key="facilityValue", required=False, default=0.00
    )
    propertyCurrentValue: float = schema_field(
        data_key="propertyCurrentValue", required=False, default=0.00
    )
    bondLenders: str = schema_field(data_key="bondLenders", required=False, default="")
    customerPeriodAtCurrentAddressYears: int = schema_field(
        data_key="customerPeriodAtCurrentAddressYears", required=False, default=0
    )
    customerPeriodAtCurrentAddressMonths: int = schema_field(
        data_key="customerPeriodAtCurrentAddressMonths", required=False, default=0
    )
    customerPeriodAtPreviousAddressYears: int = schema_field(
        data_key="customerPeriodAtPreviousAddressYears", required=False, default=0
    )
    customerPeriodAtPreviousAddressMonths: int = schema_field(
        data_key="customerPeriodAtPreviousAddressMonths", required=False, default=0
    )


@dataclass
class PassportDetails:
    customerPassportDateOfIssue: str = schema_field(
        data_key="customerPassportDateOfIssue", required=False, default=""
    )
    passportValidToDate: str = schema_field(
        data_key="passportValidToDate", required=False, default=""
    )
    customerResidencePermitType: str = schema_field(
        data_key="customerResidencePermitType", required=False, default=""
    )
    customerResidencePermitNumber: str = schema_field(
        data_key="customerResidencePermitNumber", required=False, default=""
    )
    customerResidencePermitCountryOfIssue: str = schema_field(
        data_key="customerResidencePermitCountryOfIssue", required=False, default=""
    )
    customerResidencePermitDateOfIssue: str = schema_field(
        data_key="customerResidencePermitDateOfIssue", required=False, default=""
    )
    customerResidencePermitExpiryDate: str = schema_field(
        data_key="customerResidencePermitExpiryDate", required=False, default=""
    )
    customerWorkContractExpiryDate: str = schema_field(
        data_key="customerWorkContractExpiryDate", required=False, default=""
    )


@dataclass
class SpouseDetails:
    spouseFirstNames: str = schema_field(
        data_key="spouseFirstNames", required=False, default=""
    )
    spouseMiddleName: str = schema_field(
        data_key="spouseMiddleName", required=False, default=""
    )
    spouseSurname: str = schema_field(
        data_key="spouseSurname", required=False, default=""
    )
    spouseIdType: str = schema_field(
        data_key="spouseIdType", required=False, default=""
    )
    spouseIdNo: str = schema_field(data_key="spouseIdNo", required=False, default="")
    spouseDateOfBirth: str = schema_field(
        data_key="spouseDateOfBirth", required=False, default=""
    )
    spousePhoneNumber: str = schema_field(
        data_key="spousePhoneNumber", required=False, default=""
    )


@dataclass
class EmployerDetails:
    employerName: str = schema_field(
        data_key="employerName", required=False, default=""
    )
    customerOccupation: str = schema_field(
        data_key="customerOccupation", required=False, default="Director"
    )
    employerIndustryType: str = schema_field(
        data_key="employerIndustryType", required=False, default="Transportation"
    )
    employerType: str = schema_field(
        data_key="employerType", required=False, default="Self Employed"
    )
    customerEmploymentStatus: str = schema_field(
        data_key="customerEmploymentStatus", required=False, default=""
    )
    employmentLevel: str = schema_field(
        data_key="employmentLevel", required=False, default="Skilled Worker"
    )
    customerType: str = schema_field(
        data_key="customerType",
        required=False,
        default="Self Employed(Non-Professional)",
    )
    employerAddressLine1: str = schema_field(
        data_key="employerAddressLine1", required=False, default=""
    )
    employerAddressLine2: str = schema_field(
        data_key="employerAddressLine2", required=False, default=""
    )
    employerSuburb: str = schema_field(
        data_key="employerSuburb", required=False, default=""
    )
    employerPostalCode: str = schema_field(
        data_key="employerPostalCode", required=False, default=""
    )
    employerCity: str = schema_field(
        data_key="employerCity", required=False, default=""
    )
    customerPeriodAtCurrentEmployerYears: int = schema_field(
        data_key="customerPeriodAtCurrentEmployerYears", required=False, default=0
    )
    customerPeriodAtCurrentEmployerMonths: int = schema_field(
        data_key="customerPeriodAtCurrentEmployerMonths", required=False, default=0
    )
    customerPeriodAtPreviousEmployerYears: int = schema_field(
        data_key="customerPeriodAtPreviousEmployerYears", required=False, default=0
    )
    customerPeriodAtPreviousEmployerMonths: int = schema_field(
        data_key="customerPeriodAtPreviousEmployerMonths", required=False, default=0
    )
    isBankEmployee: str = schema_field(
        data_key="isBankEmployee", required=False, default="No"
    )
    isAbsaEmployee: str = schema_field(
        data_key="isAbsaEmployee", required=False, default="No"
    )
    employeeNumber: str = schema_field(
        data_key="employeeNumber", required=False, default=""
    )


@dataclass
class ApplicantIncome:
    sourceOfIncome: str = schema_field(
        data_key="sourceOfIncome", required=False, default=""
    )
    sumIncomeCustomerGrossRemuneration: float = schema_field(
        data_key="sumIncomeCustomerGrossRemuneration", required=False, default=0.00
    )
    sumIncomeSpouseGrossRemuneration: float = schema_field(
        data_key="sumIncomeSpouseGrossRemuneration", required=False, default=0.00
    )
    sumIncomeCustomerMonthlyCommission: float = schema_field(
        data_key="sumIncomeCustomerMonthlyCommission", required=False, default=0.00
    )
    sumIncomeSpouseMonthlyCommission: float = schema_field(
        data_key="sumIncomeSpouseMonthlyCommission", required=False, default=0.00
    )
    sumIncomeCustomerCarAllowance: float = schema_field(
        data_key="sumIncomeCustomerCarAllowance", required=False, default=0.00
    )
    sumIncomeSpouseCarAllowance: float = schema_field(
        data_key="sumIncomeSpouseCarAllowance", required=False, default=0.00
    )
    sumIncomeCustomerOvertime: float = schema_field(
        data_key="sumIncomeCustomerOvertime", required=False, default=0.00
    )
    reimbursement: float = schema_field(
        data_key="reimbursement", required=False, default=0.00
    )
    addIncomeCustomerNetTakeHomePay: float = schema_field(
        data_key="addIncomeCustomerNetTakeHomePay", required=False, default=0.00
    )
    addIncomeSpouseNetTakeHomePay: float = schema_field(
        data_key="addIncomeSpouseNetTakeHomePay", required=False, default=0.00
    )
    sumIncomeCustomerRental: float = schema_field(
        data_key="sumIncomeCustomerRental", required=False, default=0.00
    )
    sumIncomeSpouseRental: float = schema_field(
        data_key="sumIncomeSpouseRental", required=False, default=0.00
    )
    sumIncomeCustomerMaintenance: float = schema_field(
        data_key="sumIncomeCustomerMaintenance", required=False, default=0.00
    )
    sumIncomeSpouseMaintenance: float = schema_field(
        data_key="sumIncomeSpouseMaintenance", required=False, default=0.00
    )
    addIncomeCustomerOtherIncome: float = schema_field(
        data_key="addIncomeCustomerOtherIncome", required=False, default=0.00
    )
    addIncomeSpouseOtherIncome: float = schema_field(
        data_key="addIncomeSpouseOtherIncome", required=False, default=0.00
    )
    addIncomeCustomerOtherIncomeDescription: float = schema_field(
        data_key="addIncomeCustomerOtherIncomeDescription", required=False, default=0.00
    )
    addIncomeSpouseOtherIncomeDescription: float = schema_field(
        data_key="addIncomeSpouseOtherIncomeDescription", required=False, default=0.00
    )
    customerTotalMonthlyIncome: float = schema_field(
        data_key="customerTotalMonthlyIncome", required=False, default=0.00
    )
    spouseTotalMonthlyIncome: float = schema_field(
        data_key="spouseTotalMonthlyIncome", required=False, default=0.00
    )


@dataclass
class ApplicantExpenses:
    sumExpensesCustomerBondPayment: float = schema_field(
        data_key="sumExpensesCustomerBondPayment", required=False, default=0.00
    )
    sumExpensesSpouseBondPayment: float = schema_field(
        data_key="sumExpensesSpouseBondPayment", required=False, default=0.00
    )
    sumExpensesCustomerRent: float = schema_field(
        data_key="sumExpensesCustomerRent", required=False, default=0.00
    )
    sumExpensesSpouseRent: float = schema_field(
        data_key="sumExpensesSpouseRent", required=False, default=0.00
    )
    totalCustomerBondAndRentPayment: float = schema_field(
        data_key="totalCustomerBondAndRentPayment", required=False, default=0.00
    )
    sumExpensesCustomerRates: float = schema_field(
        data_key="sumExpensesCustomerRates", required=False, default=0.00
    )
    sumExpensesSpouseRates: float = schema_field(
        data_key="sumExpensesSpouseRates", required=False, default=0.00
    )
    sumExpensesCustomerVehicleInstallments: float = schema_field(
        data_key="sumExpensesCustomerVehicleInstallments", required=False, default=0.00
    )
    sumExpensesSpouseVehicleInstallments: float = schema_field(
        data_key="sumExpensesSpouseVehicleInstallments", required=False, default=0.00
    )
    sumExpensesCustomerLoanRepayments: float = schema_field(
        data_key="sumExpensesCustomerLoanRepayments", required=False, default=0.00
    )
    sumExpensesSpouseLoanRepayments: float = schema_field(
        data_key="sumExpensesSpouseLoanRepayments", required=False, default=0.00
    )
    sumExpensesCustomerCreditCardRepayments: float = schema_field(
        data_key="sumExpensesCustomerCreditCardRepayments", required=False, default=0.00
    )
    sumExpensesSpouseCreditCardRepayments: float = schema_field(
        data_key="sumExpensesSpouseCreditCardRepayments", required=False, default=0.00
    )
    sumExpensesCustomerFurnitureAccounts: float = schema_field(
        data_key="sumExpensesCustomerFurnitureAccounts", required=False, default=0.00
    )
    sumExpensesSpouseFurnitureAccounts: float = schema_field(
        data_key="sumExpensesSpouseFurnitureAccounts", required=False, default=0.00
    )
    sumExpensesCustomerClothingAccounts: float = schema_field(
        data_key="sumExpensesCustomerClothingAccounts", required=False, default=0.00
    )
    sumExpensesSpouseClothingAccounts: float = schema_field(
        data_key="sumExpensesSpouseClothingAccounts", required=False, default=0.00
    )
    sumExpensesCustomerOverdraftRepayments: float = schema_field(
        data_key="sumExpensesCustomerOverdraftRepayments", required=False, default=0.00
    )
    sumExpensesSpouseOverdraftRepayments: float = schema_field(
        data_key="sumExpensesSpouseOverdraftRepayments", required=False, default=0.00
    )
    sumExpensesCustomerInsurancePayments: float = schema_field(
        data_key="sumExpensesCustomerInsurancePayments", required=False, default=0.00
    )
    sumExpensesCustomerTelephonePayments: float = schema_field(
        data_key="sumExpensesCustomerTelephonePayments", required=False, default=0.00
    )
    sumExpensesSpouseTelephonePayments: float = schema_field(
        data_key="sumExpensesSpouseTelephonePayments", required=False, default=0.00
    )
    sumExpensesCustomerTransport: float = schema_field(
        data_key="sumExpensesCustomerTransport", required=False, default=0.00
    )
    sumExpensesSpouseTransport: float = schema_field(
        data_key="sumExpensesSpouseTransport", required=False, default=0.00
    )
    sumExpensesCustomerFoodAndEntertainment: float = schema_field(
        data_key="sumExpensesCustomerFoodAndEntertainment", required=False, default=0.00
    )
    sumExpensesSpouseFoodAndEntertainment: float = schema_field(
        data_key="sumExpensesSpouseFoodAndEntertainment", required=False, default=0.00
    )
    sumExpensesCustomerEducationCosts: float = schema_field(
        data_key="sumExpensesCustomerEducationCosts", required=False, default=0.00
    )
    sumExpensesSpouseEducationCosts: float = schema_field(
        data_key="sumExpensesSpouseEducationCosts", required=False, default=0.00
    )
    sumExpensesCustomerMaintenance: float = schema_field(
        data_key="sumExpensesCustomerMaintenance", required=False, default=0.00
    )
    sumExpensesSpouseMaintenance: float = schema_field(
        data_key="sumExpensesSpouseMaintenance", required=False, default=0.00
    )
    sumExpensesCustomerHouseholdExpenses: float = schema_field(
        data_key="sumExpensesCustomerHouseholdExpenses", required=False, default=0.00
    )
    sumExpensesSpouseHouseholdExpenses: float = schema_field(
        data_key="sumExpensesSpouseHouseholdExpenses", required=False, default=0.00
    )
    sumExpensesCustomerSecurity: float = schema_field(
        data_key="sumExpensesCustomerSecurity", required=False, default=0.00
    )
    sumExpensesSpouseSecurity: float = schema_field(
        data_key="sumExpensesSpouseSecurity", required=False, default=0.00
    )
    sumExpensesCustomerOtherExpenses: float = schema_field(
        data_key="sumExpensesCustomerOtherExpenses", required=False, default=0.00
    )
    sumExpensesSpouseOtherExpenses: float = schema_field(
        data_key="sumExpensesSpouseOtherExpenses", required=False, default=0.00
    )
    sumExpensesCustomerOtherExpensesDesc: str = schema_field(
        data_key="sumExpensesCustomerOtherExpensesDesc", required=False, default=""
    )
    sumExpensesSpouseOtherExpensesDesc: str = schema_field(
        data_key="sumExpensesSpouseOtherExpensesDesc", required=False, default=""
    )
    sumExpensesCustomerOtherExpenses2: float = schema_field(
        data_key="sumExpensesCustomerOtherExpenses2", required=False, default=0.00
    )
    sumExpensesSpouseOtherExpenses2: float = schema_field(
        data_key="sumExpensesSpouseOtherExpenses2", required=False, default=0.00
    )
    sumExpensesCustomerOtherExpensesDesc2: str = schema_field(
        data_key="sumExpensesCustomerOtherExpensesDesc2", required=False, default=""
    )
    sumExpensesSpouseOtherExpensesDesc2: str = schema_field(
        data_key="sumExpensesSpouseOtherExpensesDesc2", required=False, default=""
    )
    sumExpensesCustomerOtherExpenses3: str = schema_field(
        data_key="sumExpensesCustomerOtherExpenses3", required=False, default=""
    )
    sumExpensesSpouseOtherExpenses3: str = schema_field(
        data_key="sumExpensesSpouseOtherExpenses3", required=False, default=""
    )
    sumExpensesCustomerOtherExpensesDesc3: str = schema_field(
        data_key="sumExpensesCustomerOtherExpensesDesc3", required=False, default=""
    )
    sumExpensesSpouseOtherExpensesDesc3: str = schema_field(
        data_key="sumExpensesSpouseOtherExpensesDesc3", required=False, default=""
    )
    sumExpensesCustomerLoansRepaidViaPayrollDeduc: float = schema_field(
        data_key="sumExpensesCustomerLoansRepaidViaPayrollDeduc",
        required=False,
        default=0.00,
    )
    sumExpensesSpouseLoansRepaidViaPayrollDeduc: float = schema_field(
        data_key="sumExpensesSpouseLoansRepaidViaPayrollDeduc",
        required=False,
        default=0.00,
    )
    customerTotalExpenses: float = schema_field(
        data_key="customerTotalExpenses", required=False, default=0.00
    )
    spouseTotalExpenses: float = schema_field(
        data_key="spouseTotalExpenses", required=False, default=0.00
    )
    customerDisposableIncome: float = schema_field(
        data_key="customerDisposableIncome", required=False, default=0.00
    )
    spouseDisposableIncome: float = schema_field(
        data_key="spouseDisposableIncome", required=False, default=0.00
    )


@dataclass
class SourceOfFunds:
    sourceOfFundsAllowance: str = schema_field(
        data_key="sourceOfFundsAllowance", required=False, default="No"
    )
    sourceOfFundsBonus: str = schema_field(
        data_key="sourceOfFundsBonus", required=False, default="No"
    )
    sourceOfFundsBonusAmount: float = schema_field(
        data_key="sourceOfFundsBonusAmount", required=False, default=0.00
    )
    sourceOfFundsCommissionsEarned: str = schema_field(
        data_key="sourceOfFundsCommissionsEarned", required=False, default="No"
    )
    sourceOfFundsCommissionsEarnedAmount: float = schema_field(
        data_key="sourceOfFundsCommissionsEarnedAmount", required=False, default=0.00
    )
    sourceOfFundsCourtOrder: str = schema_field(
        data_key="sourceOfFundsCourtOrder", required=False, default="No"
    )
    sourceOfFundsCourtOrderAmount: float = schema_field(
        data_key="sourceOfFundsCourtOrderAmount", required=False, default=0.00
    )
    sourceOfFundsDividends: str = schema_field(
        data_key="sourceOfFundsDividends", required=False, default="No"
    )
    sourceOfFundsDividendsAmount: float = schema_field(
        data_key="sourceOfFundsDividendsAmount", required=False, default=0.00
    )
    sourceOfFundsDonations: str = schema_field(
        data_key="sourceOfFundsDonations", required=False, default="No"
    )
    sourceOfFundsDonationsAmount: float = schema_field(
        data_key="sourceOfFundsDonationsAmount", required=False, default=0.00
    )
    sourceOfFundsInheritance: str = schema_field(
        data_key="sourceOfFundsInheritance", required=False, default="No"
    )
    sourceOfFundsInheritanceAmount: float = schema_field(
        data_key="sourceOfFundsInheritanceAmount", required=False, default=0.00
    )
    sourceOfFundsInsuranceClaim: str = schema_field(
        data_key="sourceOfFundsInsuranceClaim", required=False, default="No"
    )
    sourceOfFundsInsuranceClaimAmount: float = schema_field(
        data_key="sourceOfFundsInsuranceClaimAmount", required=False, default=0.00
    )
    sourceOfFundsInterest: str = schema_field(
        data_key="sourceOfFundsInterest", required=False, default="No"
    )
    sourceOfFundsInterestAmount: float = schema_field(
        data_key="sourceOfFundsInterestAmount", required=False, default=0.00
    )
    sourceOfFundsInvestmentIncome: str = schema_field(
        data_key="sourceOfFundsInvestmentIncome", required=False, default="No"
    )
    sourceOfFundsInvestmentIncomeAmount: float = schema_field(
        data_key="sourceOfFundsInvestmentIncomeAmount", required=False, default=0.00
    )
    sourceOfFundsMaintenance: str = schema_field(
        data_key="sourceOfFundsMaintenance", required=False, default="No"
    )
    sourceOfFundsMaintenanceAmount: float = schema_field(
        data_key="sourceOfFundsMaintenanceAmount", required=False, default=0.00
    )
    sourceOfFundsPension: str = schema_field(
        data_key="sourceOfFundsPension", required=False, default="No"
    )
    sourceOfFundsPensionAmount: float = schema_field(
        data_key="sourceOfFundsPensionAmount", required=False, default=0.00
    )
    sourceOfFundsProceedsFromOwnBusiness: str = schema_field(
        data_key="sourceOfFundsProceedsFromOwnBusiness", required=False, default="No"
    )
    sourceOfFundsRentals: str = schema_field(
        data_key="sourceOfFundsRentals", required=False, default="No"
    )
    sourceOfFundsRetirementAnnuity: str = schema_field(
        data_key="sourceOfFundsRetirementAnnuity", required=False, default="No"
    )
    sourceOfFundsRetirementAnnuityAmount: float = schema_field(
        data_key="sourceOfFundsRetirementAnnuityAmount", required=False, default=0.00
    )
    sourceOfFundsSalary: str = schema_field(
        data_key="sourceOfFundsSalary", required=False, default="No"
    )
    sourceOfFundsSocialBenefits: str = schema_field(
        data_key="sourceOfFundsSocialBenefits", required=False, default="No"
    )
    sourceOfFundsSocialGrant: str = schema_field(
        data_key="sourceOfFundsSocialGrant", required=False, default="No"
    )
    sourceOfFundsWinnings: str = schema_field(
        data_key="sourceOfFundsWinnings", required=False, default="No"
    )
    sourceOfFundsWinningsAmount: float = schema_field(
        data_key="sourceOfFundsWinningsAmount", required=False, default=0.00
    )
    sourceOfFundsBEE: str = schema_field(
        data_key="sourceOfFundsBEE", required=False, default="No"
    )
    sourceOfFundsBEEAmount: float = schema_field(
        data_key="sourceOfFundsBEEAmount", required=False, default=0.00
    )


@dataclass
class LiabilityDetails:
    suretyLiabilityIndicator: str = schema_field(
        data_key="suretyLiabilityIndicator", required=False, default="No"
    )
    surety: str = schema_field(data_key="surety", required=False, default="")
    guarantorLiabilityIndicator: str = schema_field(
        data_key="guarantorLiabilityIndicator", required=False, default="No"
    )
    guarantor: str = schema_field(data_key="guarantor", required=False, default="")
    coDebtorLiabilityIndicator: str = schema_field(
        data_key="coDebtorLiabilityIndicator", required=False, default="No"
    )
    coDebtor: str = schema_field(data_key="coDebtor", required=False, default="")


@dataclass
class PaymentHistory:
    debtReviewIndicator: str = schema_field(
        data_key="debtReviewIndicator", required=False, default="No"
    )
    debtCounselling: str = schema_field(
        data_key="debtCounselling", required=False, default="No"
    )
    administrationOrderIndicator: str = schema_field(
        data_key="administrationOrderIndicator", required=False, default="No"
    )
    debtAdmin: str = schema_field(data_key="debtAdmin", required=False, default="No")
    previousJudgementIndicator: str = schema_field(
        data_key="previousJudgementIndicator", required=False, default="No"
    )
    DebtDisp: str = schema_field(data_key="DebtDisp", required=False, default="No")
    debtSeqOrder: str = schema_field(
        data_key="debtSeqOrder", required=False, default="No"
    )


@dataclass
class RelativeDetails:
    relativeFirstNames: str = schema_field(
        data_key="relativeFirstNames", required=False, default=""
    )
    relativeSurname: str = schema_field(
        data_key="relativeSurname", required=False, default=""
    )
    relativeRelation: str = schema_field(
        data_key="relativeRelation", required=False, default=""
    )
    relativePreferredContactMethod: str = schema_field(
        data_key="relativePreferredContactMethod", required=False, default=""
    )
    relativeCellphone: str = schema_field(
        data_key="relativeCellphone", required=False, default=""
    )
    relativePhoneNumber: str = schema_field(
        data_key="relativePhoneNumber", required=False, default=""
    )
    relativeWorkNumber: str = schema_field(
        data_key="relativeWorkNumber", required=False, default=""
    )
    relativeAddressLine1: str = schema_field(
        data_key="relativeAddressLine1", required=False, default=""
    )
    relativeAddressLine2: str = schema_field(
        data_key="relativeAddressLine2", required=False, default=""
    )
    relativeAddressSuburb: str = schema_field(
        data_key="relativeAddressSuburb", required=False, default=""
    )
    relativeAddressCity: str = schema_field(
        data_key="relativeAddressCity", required=False, default=""
    )
    relativeAddressPostalCode: str = schema_field(
        data_key="relativeAddressPostalCode", required=False, default=""
    )


@dataclass
class BankingDetails:
    customerBankAccountBank: str = schema_field(
        data_key="customerBankAccountBank", required=False, default=""
    )
    customerBankAccountBranchName: str = schema_field(
        data_key="customerBankAccountBranchName", required=False, default=""
    )
    chkAccApplicant: str = schema_field(
        data_key="chkAccApplicant", required=False, default="No"
    )
    customerBankAccountHolder: str = schema_field(
        data_key="customerBankAccountHolder", required=False, default=""
    )
    customerBankAccountNumber: str = schema_field(
        data_key="customerBankAccountNumber", required=False, default=""
    )
    validBankAccount: str = schema_field(
        data_key="validBankAccount", required=False, default="No"
    )
    customerBankAccountType: str = schema_field(
        data_key="customerBankAccountType", required=False, default=""
    )
    customerBankAccountBranchCode: str = schema_field(
        data_key="customerBankAccountBranchCode", required=False, default=""
    )
    paymentMethod: str = schema_field(
        data_key="paymentMethod", required=False, default=""
    )
    settleExistingInstallment: str = schema_field(
        data_key="settleExistingInstallment", required=False, default="No"
    )
    bankNameAccToSettle: str = schema_field(
        data_key="bankNameAccToSettle", required=False, default=""
    )
    accountNumberToSettle: str = schema_field(
        data_key="accountNumberToSettle", required=False, default=""
    )
    monthlyInstallmentOnAccountToBeSettled: float = schema_field(
        data_key="monthlyInstallmentOnAccountToBeSettled", required=False, default=0.00
    )
    settlementAmount: float = schema_field(
        data_key="settlementAmount", required=False, default=0.00
    )
    accountNumberToSettle2: str = schema_field(
        data_key="accountNumberToSettle2", required=False, default=""
    )
    monthlyInstallmentOnAccountToBeSettled2: float = schema_field(
        data_key="monthlyInstallmentOnAccountToBeSettled2", required=False, default=0.00
    )
    settlementAmount2: float = schema_field(
        data_key="settlementAmount2", required=False, default=0.00
    )
    customerSalaryDay: str = schema_field(
        data_key="customerSalaryDay", required=False, default=""
    )
    customerBankAccountStatus: str = schema_field(
        data_key="customerBankAccountStatus", required=False, default=""
    )
    paymentDate: str = schema_field(
        data_key="paymentDate", required=False, default="01"
    )


@dataclass
class Statement:
    customerStatementDeliveryMethod: str = schema_field(
        data_key="customerStatementDeliveryMethod", required=False, default=""
    )
    customerPreferredEmailAddress: str = schema_field(
        data_key="customerPreferredEmailAddress", required=False, default=""
    )
    customerAlternateEmailAddress: str = schema_field(
        data_key="customerAlternateEmailAddress", required=False, default=""
    )
    customerPreferredDeliveryMethod: str = schema_field(
        data_key="customerPreferredDeliveryMethod", required=False, default=""
    )


@dataclass
class AppDetails:
    marketingConsentIndicator: str = schema_field(
        data_key="marketingConsentIndicator", required=False, default="No"
    )
    itcConcentIndicator: str = schema_field(
        data_key="itcConcentIndicator", required=False, default="No"
    )
    outstandingServiceConsent: str = schema_field(
        data_key="outstandingServiceConsent", required=False, default="No"
    )


@dataclass
class BankStatementConsent:
    customerBankStatementConsentIndicator: str = schema_field(
        data_key="customerBankStatementConsentIndicator", required=False, default="No"
    )


@dataclass
class SataxiRoute:
    taxiAssociation: str = schema_field(
        data_key="taxiAssociation", required=False, default=""
    )
    routeFromTo: str = schema_field(data_key="routeFromTo", required=False, default="")
    driverWagePerMonth: float = schema_field(
        data_key="driverWagePerMonth", required=False, default=0.00
    )
    averageNumberOfPassengersPerTrip: float = schema_field(
        data_key="averageNumberOfPassengersPerTrip", required=False, default=0.00
    )
    farePerPassenger: float = schema_field(
        data_key="farePerPassenger", required=False, default=0.00
    )
    dayWorkedPerMonth: int = schema_field(
        data_key="dayWorkedPerMonth", required=False, default=0
    )
    taxiAssociationProvince: str = schema_field(
        data_key="taxiAssociationProvince", required=False, default=""
    )
    area: str = schema_field(data_key="area", required=False, default="")
    kmPerTrip: float = schema_field(data_key="kmPerTrip", required=False, default=0.00)
    noOfTripsPerDay: int = schema_field(
        data_key="noOfTripsPerDay", required=False, default=0
    )
    monIncNoOfSeats: int = schema_field(
        data_key="monIncNoOfSeats", required=False, default=0
    )


@dataclass
class SataxiInsurance:
    supplier: str = schema_field(data_key="supplier", required=False, default="")
    insuranceBroker: str = schema_field(
        data_key="insuranceBroker", required=False, default=""
    )
    insuranceBrokerCode: str = schema_field(
        data_key="insuranceBrokerCode", required=False, default=""
    )
    insuranceAmount: float = schema_field(
        data_key="insuranceAmount", required=False, default=0.00
    )
    creditLifeDisplayNote: str = schema_field(
        data_key="creditLifeDisplayNote", required=False, default="No"
    )


@dataclass
class BeeActStatus:
    isBEEActBeneficiary: str = schema_field(
        data_key="isBEEActBeneficiary", required=False, default="No"
    )


@dataclass
class SignioLoanDetailsRequest:
    caseNumber: int = schema_field(data_key="caseNumber", required=True, default=1)
    campaign: Campaign = schema_field(data_key="campaign", required=True, default=0)
    eApplication: Application = schema_field(
        data_key="eApplication", required=False, default=None
    )
    vehicleDetails: VehicleDetails = schema_field(
        data_key="vehicleDetails", required=False, default=None
    )
    financeDetails: FinanceDetails = schema_field(
        data_key="financeDetails", required=False, default=None
    )
    personalDetails: PersonalDetails = schema_field(
        data_key="personalDetails", required=False, default=None
    )
    residentialAddress: ResidentialDetails = schema_field(
        data_key="residentialAddress", required=False, default=None
    )
    passportDetails: PassportDetails = schema_field(
        data_key="passportDetails", required=False, default=None
    )
    spouseDetails: SpouseDetails = schema_field(
        data_key="spouseDetails", required=False, default=None
    )
    employerDetails: EmployerDetails = schema_field(
        data_key="employerDetails", required=False, default=None
    )
    applicantIncome: ApplicantIncome = schema_field(
        data_key="applicantIncome", required=False, default=None
    )
    applicantExpenses: ApplicantExpenses = schema_field(
        data_key="applicantExpenses", required=False, default=None
    )
    sourceOfFunds: SourceOfFunds = schema_field(
        data_key="sourceOfFunds", required=False, default=None
    )
    liabilityDetails: LiabilityDetails = schema_field(
        data_key="liabilityDetails", required=False, default=None
    )
    paymentHistory: PaymentHistory = schema_field(
        data_key="paymentHistory", required=False, default=None
    )
    relativeDetails: RelativeDetails = schema_field(
        data_key="relativeDetails", required=False, default=None
    )
    bankingDetails: BankingDetails = schema_field(
        data_key="bankingDetails", required=False, default=None
    )
    statement: Statement = schema_field(
        data_key="statement", required=False, default=None
    )
    appDetails: AppDetails = schema_field(
        data_key="appDetails", required=False, default=None
    )
    bankStatementConsent: BankStatementConsent = schema_field(
        data_key="bankStatementConsent", required=False, default=None
    )
    saTaxiRoute: SataxiRoute = schema_field(
        data_key="saTaxiRoute", required=False, default=None
    )
    saTaxiInsurance: SataxiInsurance = schema_field(
        data_key="saTaxiInsurance", required=False, default=None
    )
    beeActStatus: BeeActStatus = schema_field(
        data_key="beeActStatus", required=False, default=None
    )

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
