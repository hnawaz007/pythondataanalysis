from typing import Iterator, Any
import dlt
from dlt.sources.credentials import ConnectionStringCredentials
from sql_database import sql_database, sql_table, Table
from datetime import datetime
import pytz





def incremental_load_upsert_date(table, column) -> None:
    """Build a pipeline"""
    pipeline = dlt.pipeline(
        pipeline_name="sql_database",
        destination='postgres',
        dataset_name="incremental",
    )
    
    tbl = sql_table(
        table=table,
        incremental=dlt.sources.incremental(
            'ModifiedDate',  # Cursor column name
            initial_value=datetime(2023, 2, 8, 0, 0, 0, 0, pytz.UTC)  # Initial cursor value
        )
    )

    # Incrementally loading a table based on the primary_key column
    info = pipeline.run(
        tbl, 
        write_disposition="merge", 
        primary_key=column,
        table_name=table
        )
    # print info
    print(info)


if __name__ == "__main__":
    # Load selected tables with different settings
    incremental_load_upsert_date("product", "ProductID")