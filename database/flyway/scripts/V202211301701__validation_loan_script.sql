DROP TABLE IF EXISTS finance.VG_Validation_Loan CASCADE;

CREATE TABLE finance.VG_Validation_Loan
( AccountNumber varchar(15)
, IDNo varchar(20)
, CustomerName varchar(100)
, Mobile varchar(25)
, TaxiAssociation varchar(200)
, ResidentialAddress varchar(200)
, PostalAddress varchar(200)
, NextInstalmentDate timestamp
, InstalmentDay integer
, PaymentType varchar(5)
, LoanStartDate timestamp
, BankAccountNumber varchar(30)
, BankAccountType varchar(7)
, BankName varchar(70)
);

ALTER TABLE finance.VG_Validation_Loan ALTER AccountNumber SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER IDNo SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER CustomerName SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER Mobile SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER TaxiAssociation SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER ResidentialAddress SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER PostalAddress SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER NextInstalmentDate SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER InstalmentDay SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER PaymentType SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER LoanStartDate SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER BankAccountNumber SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER BankAccountType SET NOT NULL;
ALTER TABLE finance.VG_Validation_Loan ALTER BankName SET NOT NULL;

ALTER TABLE finance.VG_Validation_Loan
 ADD CONSTRAINT VG_VALIDATION_LOAN_PKEY PRIMARY KEY
  ( AccountNumber
  )
;
