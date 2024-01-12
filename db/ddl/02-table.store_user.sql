-- Table: buyrite.store_user

-- DROP TABLE buyrite.store_user;

CREATE TABLE IF NOT EXISTS buyrite.store_user
(
	store_user_id			BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY (MINVALUE 1 START WITH 1 CACHE 1),
	store_user_guid			UUID UNIQUE NOT NULL,
	store_id          		BIGINT  NULL,
	email					CHARACTER VARYING(200) NOT NULL,
	role					CHARACTER VARYING(200) NOT NULL,
	title					CHARACTER VARYING(80) NOT NULL,
	working_hours			TIME NOT NULL,
	hourly_rate 			NUMERIC(22, 6) NOT NULL,
	weekly_payment			NUMERIC(22, 6) NOT NULL,
	hire_date				DATE NOT NULL,
	termination_date		DATE NOT NULL,

	CONSTRAINT fk_store_user_id FOREIGN KEY(store_id) REFERENCES buyrite.store(store_id)
)
TABLESPACE pg_default;

ALTER TABLE buyrite.store_user
	OWNER to buyrite_tracker;

CREATE UNIQUE INDEX IF NOT EXISTS store_user_store_user_guid_idx
	ON buyrite.store_user (store_user_guid);

CREATE INDEX IF NOT EXISTS store_user_store_id_idx
	ON buyrite.store_user (store_id);
