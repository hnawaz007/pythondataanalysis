import dlt
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os
#get password from environmnet var
pwd = os.environ['PGPASS']
uid = os.environ['PGUID']
#sql db details
server = "192.168.1.39"
driver =  "{SQL Server Native Client 11.0}"
src_db = "AdventureWorksDW2019;"


# Use any SQL database supported by SQLAlchemy, below we use a public
# SQLServer instance to get data.
# NOTE: you'll need to install SQLServer with `pip install pyodbc`
# NOTE: loading data from dbo SQLServer instance may take several seconds
connection_string = 'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + src_db + ';UID=' + uid + ';PWD=' + pwd
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
src_engine = create_engine(connection_url)


with src_engine.connect() as conn:
    # Select genome table, stream data in batches of 100 elements
    query = "SELECT * FROM [dbo].[DimProductCategory]"
    rows = conn.execution_options(yield_per=100).exec_driver_sql(query)

    pipeline = dlt.pipeline(
        pipeline_name="from_sqlserver",
        destination="postgres",
        dataset_name="public"
    )

    # Convert the rows into dictionaries on the fly with a map function
    load_info = pipeline.run(map(lambda row: dict(row._mapping), rows), table_name="dimproductcategory")

print(load_info)