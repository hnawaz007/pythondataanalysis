CREATE TABLE IF NOT EXISTS minio.sales.sales_tz (
  productcategoryname VARCHAR,
  productsubcategoryname VARCHAR,
  productname VARCHAR,
  country VARCHAR,
  salesamount DOUBLE,
  orderdate timestamp
)
WITH (
  external_location = 's3a://sales/',
  format = 'PARQUET'
);
--------------------kafka TABLE--------------
CREATE TABLE minio.kafka.tblsales (
   productkey INTEGER,
   customerkey INTEGER,
   salesterritorykey INTEGER,
   salesordernumber varchar,
   totalproductcost DOUBLE,
   salesamount DOUBLE,
   id INTEGER
)
WITH (
   external_location = 's3a://kafka-bucket/topics/src.public.factinternetsales_streaming/partition=0/',
   format = 'JSON'
);

------------Select Query
select * from minio.kafka.tblsales
order by salesordernumber