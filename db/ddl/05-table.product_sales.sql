-- Table: buyrite.product_sales;

-- DROP TABLE buyrite.product_sales;

CREATE TABLE IF NOT EXISTS buyrite.product_sales
(
    product_sales_id		BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY (MINVALUE 1 START WITH 1 CACHE 1),
	product_sales_guid		UUID UNIQUE NOT NULL,
    product_id              BIGINT  NULL,
    store_id                BIGINT  NULL,
    sales_from_date         DATE NOT NULL,
    sales_end_date          DATE NOT NULL,
    units_sold              NUMERIC(22) NOT NULL,
    units_discount_price    NUMERIC(22) NOT NULL,

    CONSTRAINT fk_product_sales_product_id FOREIGN KEY(product_id) REFERENCES buyrite.product(product_id),
    CONSTRAINT fk_product_sales_store_id FOREIGN KEY(store_id) REFERENCES buyrite.store(store_id)
)

TABLESPACE pg_default;

ALTER TABLE buyrite.product_sales
	OWNER to buyrite_tracker;

CREATE UNIQUE INDEX IF NOT EXISTS product_sales_product_sales_guid_idx
	ON buyrite.product_sales (product_sales_guid);

CREATE INDEX IF NOT EXISTS product_sales_product_id_idx
	ON buyrite.product_sales (product_id);

CREATE INDEX IF NOT EXISTS product_sales_store_id_idx
	ON buyrite.product_sales (store_id);
