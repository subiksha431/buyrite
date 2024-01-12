-- Table: buyrite.vendor

-- DROP TABLE buyrite.vendor;

CREATE TABLE IF NOT EXISTS buyrite.vendor
(
    vendor_id	                BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY (MINVALUE 1 START WITH 1 CACHE 1),
    vendor_guid                 UUID UNIQUE NOT NULL,
    code                        UUID UNIQUE NOT NULL,
    name                        CHARACTER VARYING(200)  NULL,
    address                     CHARACTER VARYING(200)  NULL,
    phone_number                NUMERIC(22) NULL,
    sales_representative        CHARACTER VARYING(200)  NULL,
    sales_contact_phone_number  NUMERIC(22) NULL,
    sales_contact_email         CHARACTER VARYING(200)  NULL,
    procurement_email           CHARACTER VARYING(200)  NULL,
    last_updated_date           DATE NOT NULL,
    last_updated_by             DATE NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE buyrite.vendor
	OWNER to buyrite_tracker;

CREATE UNIQUE INDEX IF NOT EXISTS vendor_vendor_guid_idx
	ON buyrite.vendor (vendor_guid);

CREATE UNIQUE INDEX IF NOT EXISTS vendor_code_idx
	ON buyrite.vendor (code);

