-- Table: public.factinternetsales_streaming

-- DROP TABLE IF EXISTS public.factinternetsales_streaming;

CREATE TABLE IF NOT EXISTS public.factinternetsales_streaming
(
    productkey bigint,
    customerkey bigint,
    salesterritorykey bigint,
    salesordernumber text COLLATE pg_catalog."default",
    totalproductcost double precision,
    salesamount double precision
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.factinternetsales_streaming
    OWNER to postgres;
