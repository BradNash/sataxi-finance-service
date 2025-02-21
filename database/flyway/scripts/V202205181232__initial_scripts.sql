DROP TABLE IF EXISTS finance.SignioLoanDetails CASCADE;
CREATE TABLE finance.SignioLoanDetails
(
    case_no integer,
    loan_application_details jsonb,
    campaign integer,
    processed integer,
    processed_date timestamp
);

ALTER TABLE finance.SignioLoanDetails ALTER case_no SET NOT NULL;
ALTER TABLE finance.SignioLoanDetails ALTER loan_application_details SET NOT NULL;
ALTER TABLE finance.SignioLoanDetails ALTER campaign SET NOT NULL;
ALTER TABLE finance.SignioLoanDetails ALTER processed SET NOT NULL;
ALTER TABLE finance.SignioLoanDetails ALTER processed SET DEFAULT 0;
ALTER TABLE finance.SignioLoanDetails ADD CONSTRAINT SIGNIO_LOAN_DETAILS_PKEY PRIMARY KEY (case_no);

CREATE TABLE finance.SignioLoanApplication
( case_no integer
    , signio_application_request xml
    , response_message varchar(250)
    , response_code integer
    , referenceNumber varchar(20)
);
ALTER TABLE finance.SignioLoanApplication ALTER case_no SET NOT NULL;
ALTER TABLE finance.SignioLoanApplication ALTER signio_application_request SET NOT NULL;
ALTER TABLE finance.SignioLoanApplication ADD CONSTRAINT SIGNIO_LOAN_APPLICATION_PKEY PRIMARY KEY (case_no);
ALTER TABLE finance.SignioLoanApplication ADD CONSTRAINT SIGNIO_LOAN_APPLICATION_FK01 FOREIGN KEY (case_no)
    REFERENCES finance.SignioLoanApplication MATCH FULL;


