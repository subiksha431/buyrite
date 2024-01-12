-- Table: buyrite.product

-- DROP TABLE buyrite.product;

CREATE TABLE IF NOT EXISTS buyrite.product
(
	product_id			    BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY (MINVALUE 1 START WITH 1 CACHE 1),
    product_guid            UUID UNIQUE NOT NULL,
    store_id                BIGINT  NULL,
	item    			    BIGINT UNIQUE NOT NULL,
	description			    CHARACTER VARYING(200) NOT NULL,
	type				    CHARACTER VARYING(200)  NULL,
	unit_price			    NUMERIC(22, 6) NOT NULL,
	unit_markup			    NUMERIC(22, 6) NOT NULL,
	sale_price              NUMERIC(22, 6) NOT NULL,
    units_in_carton         NUMERIC(22) NOT NULL,
    carton_price            NUMERIC(22, 6) NOT NULL,
    sold_as_carton          BIT NOT NULL,
    sale_unit               NUMERIC(22,6) NOT NULL,
    --unit_size               NUMERIC(22,4) NULL,
    unit_size               CHARACTER VARYING(200) NOT NULL,
    last_updated_date       DATE NOT NULL,
    last_updated_by         CHARACTER VARYING(200) NOT NULL,

    CONSTRAINT fk_product_id FOREIGN KEY(store_id) REFERENCES buyrite.store(store_id)
)
TABLESPACE pg_default;

ALTER TABLE buyrite.product
	OWNER to buyrite_tracker;

CREATE UNIQUE INDEX IF NOT EXISTS product_product_guid_idx
	ON buyrite.product (product_guid);

CREATE INDEX IF NOT EXISTS product_store_id_idx
	ON buyrite.product (store_id);