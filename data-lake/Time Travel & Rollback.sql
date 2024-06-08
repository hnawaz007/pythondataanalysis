SELECT *
FROM iceberg.raw.ice_tbl_sales;

--snapshots of the table
SELECT * FROM iceberg.raw."ice_tbl_sales$snapshots";

--blank table
SELECT *
FROM iceberg.raw.ice_tbl_sales FOR VERSION AS OF 5856133835153055555;

--all rows inserted
SELECT *
FROM iceberg.raw.ice_tbl_sales FOR VERSION AS OF 1541366083334671645;

-- deleted rows
SELECT *
FROM iceberg.raw.ice_tbl_sales FOR VERSION AS OF 536093431727407250;

-- netsales column
SELECT *
FROM iceberg.raw.ice_tbl_sales FOR VERSION AS OF 876042034778742235;

--roll back to state with all 42 rows.
CALL iceberg.system.rollback_to_snapshot('raw', 'ice_tbl_sales', 1541366083334671645)