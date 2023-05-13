SELECT productcategoryname, sum(salesamount) as sales
FROM minio.sales.sales_parquet
where country = 'United States'
group by productcategoryname
