--external table
CREATE TABLE IF NOT exists hive.raw.tbl_sales (
   productkey INTEGER,
   customerkey INTEGER,
   salesterritorykey INTEGER,
   salesordernumber varchar,
   totalproductcost DOUBLE,
   salesamount DOUBLE,
   id INTEGER
)
WITH (
  external_location = 's3a://kafka-avro/topics/avro.public.factinternetsales_streaming/partition=0/',
  format = 'PARQUET'
);


--create iceberg table.
CREATE TABLE iceberg.raw.ice_tbl_sales (
   productkey INTEGER,
   customerkey INTEGER,
   salesterritorykey INTEGER,
   salesordernumber varchar,
   totalproductcost DOUBLE,
   salesamount DOUBLE,
   id INTEGER
);

-- insert data in iceberg
INSERT INTO iceberg.raw.ice_tbl_sales 
SELECT * FROM hive.raw.tbl_sales ;

-- select
SELECT * from iceberg.raw.ice_tbl_sales 
order by id asc

-- select data
select *
from hive.raw.tbl_sales 
where id between  1 and 10

--- count 
select count(*)
from iceberg.raw.ice_tbl_sales

--delete rows
delete from iceberg.raw.ice_tbl_sales 
where id between  1 and 10

---
select *
from iceberg.raw.ice_tbl_sales 

--schema evolution
ALTER TABLE iceberg.raw.ice_tbl_sales  RENAME COLUMN id TO salesid

ALTER TABLE iceberg.raw.ice_tbl_sales  ADD COLUMN netsales DOUBLE

update iceberg.raw.ice_tbl_sales  set netsales = salesamount - totalproductcost