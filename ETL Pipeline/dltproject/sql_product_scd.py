from typing import Iterator, Any
import dlt
from dlt.sources.credentials import ConnectionStringCredentials
from sql_database import sql_database, sql_table, Table
from datetime import datetime





def load_scd_dim(table, column) -> None:
    """Build a pipeline"""
    pipeline = dlt.pipeline(
        pipeline_name="sql_database_prodcut_scd2",
        destination='postgres',
        dataset_name="snapshots",
    )
    
    # Get the source Data
    tbl = sql_table(
        table=table,
        schema="dbo",
        )

    # loading a table based on the primary_key column with type2
    info = pipeline.run(
        tbl,
        write_disposition={"disposition": "merge", "strategy": "scd2"},
        primary_key=column,
        table_name=table
    )
    # print info
    print(info)


if __name__ == "__main__":
    # Load selected tables with different settings
    load_scd_dim("product", "ProductID")