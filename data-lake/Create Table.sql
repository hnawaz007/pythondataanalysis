CREATE TABLE IF NOT EXISTS minio.sales.sales_parquet (
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
