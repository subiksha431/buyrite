-- Table: buyrite.store

-- DROP TABLE buyrite.store;

CREATE TABLE IF NOT EXISTS buyrite.store
(
	store_id			BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY (MINVALUE 1 START WITH 1 CACHE 1),
	store_guid			UUID UNIQUE NOT NULL,
	store_name			CHARACTER VARYING(200)  NULL,
	location			CHARACTER VARYING(200)  NULL,
	type				CHARACTER VARYING(200)  NULL,
	owner				CHARACTER VARYING(80)  NULL,
	rent				NUMERIC(22, 6) NULL,
	rent_payment_window NUMERIC(22) NULL
)
TABLESPACE pg_default;

ALTER TABLE buyrite.store
	OWNER to buyrite_tracker;

CREATE UNIQUE INDEX IF NOT EXISTS store_store_guid_idx
	ON buyrite.store (store_guid);
  