from typing import Iterator, Any

import dlt
from dlt.sources.credentials import ConnectionStringCredentials

from sql_database import sql_database, sql_table, Table


def load_select_tables_from_database() -> None:
    """Use the sql_database source to reflect an entire database schema and load select tables from it.

    This example sources data from the public Rfam SQL database.
    """
    # Create a pipeline
    pipeline = dlt.pipeline(
        pipeline_name="rfam", destination='postgres', dataset_name="sql_data"
    )



    # Configure the source to load a few select tables incrementally
    source_1 = sql_database(credentials).with_resources("DimProductCategory", "DimProduct")
    # Add incremental config to the resources. "updated" is a timestamp column in these tables that gets used as a cursor
    source_1.DimProductCategory.apply_hints(incremental=dlt.sources.incremental("updated"))
    source_1.DimProduct.apply_hints(incremental=dlt.sources.incremental("updated"))

    # Run the pipeline. The merge write disposition merges existing rows in the destination by primary key
    info = pipeline.run(source_1, write_disposition="merge")
    print(info)

    # Load some other tables with replace write disposition. This overwrites the existing tables in destination
    #source_2 = sql_database(credentials).with_resources("DimProduct", "author")
    #info = pipeline.run(source_2, write_disposition="replace")
    #print(info)

    # Load a table incrementally with append write disposition
    # this is good when a table only has new rows inserted, but not updated
    source_3 = sql_database(credentials).with_resources("DimSalesTerritory")
    source_3.DimSalesTerritory.apply_hints(incremental=dlt.sources.incremental("created"))

    info = pipeline.run(source_3, write_disposition="append")
    print(info)


def load_entire_database() -> None:
    """Use the sql_database source to completely load all tables in a database"""
    pipeline = dlt.pipeline(
        pipeline_name="rfam", destination='postgres', dataset_name="sql_data"
    )

    # By default the sql_database source reflects all tables in the schema
    # The database credentials are sourced from the `.dlt/secrets.toml` configuration
    source = sql_database()

    # Run the pipeline. For a large db this may take a while
    info = pipeline.run(source, write_disposition="replace")
    print(info)


def load_standalone_table_resource() -> None:
    """Load a few known tables with the standalone sql_table resource, request full schema and deferred
    table reflection"""
    pipeline = dlt.pipeline(
        pipeline_name="rfam_database",
        destination='postgres',
        dataset_name="rfam_data",
        full_refresh=True,
    )

    # Load a table incrementally starting at a given date
    # Adding incremental via argument like this makes extraction more efficient
    # as only rows newer than the start date are fetched from the table
    # we also use `detect_precision_hints` to get detailed column schema
    # and defer_table_reflect to reflect schema only during execution
    tbl = sql_table(
        table="DimProductCategory",
        incremental=dlt.sources.incremental(
            "updated",
        ),
        detect_precision_hints=True,
        defer_table_reflect=True,
    )
    # columns will be empty here due to defer_table_reflect set to True
    print(tbl.compute_table_schema())

    # Run the resources together
    info = pipeline.extract([tbl], write_disposition="merge")
    print(info)
    # Show inferred columns
    print(pipeline.default_schema.to_pretty_yaml())


def select_columns() -> None:
    """Uses table adapter callback to modify list of columns to be selected"""
    pipeline = dlt.pipeline(
        pipeline_name="sql_server_database",
        destination='postgres',
        dataset_name="source_aql_data",
        #full_refresh=True, # This appends datetime to schema name. On each run creates new schema.
    )

    def table_adapter(table: Table) -> None:
        print(table.name)
        #if table.name == "DimProductCategory":
            # this is SqlAlchemy table. _columns are writable
            # let's drop updated column
            #table._columns.remove(table.columns["updated"])

    dimproductcategory = sql_table(
        table="DimProductCategory",
        chunk_size=10,
        detect_precision_hints=True,
        table_adapter_callback=table_adapter,
    )

    # run pipeline
    pipeline.run(dimproductcategory)
    # 
    print(pipeline.last_trace.last_normalize_info)
    # no "updated" column in "family" table
    print(pipeline.default_schema.to_pretty_yaml())


#
def incremental_load_upsert(table, column) -> None:
    """Build a pipeline"""
    pipeline = dlt.pipeline(
        pipeline_name="sql_database",
        destination='postgres',
        dataset_name="incremental",
    )
    
    # Get the source Data
    tbl = sql_table(
        table=table,
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
    # load_select_tables_from_database()

    # load a table and select columns
    #select_columns()

    # Load tables with the standalone table resource
    #load_standalone_table_resource()

    # Load all tables from the database.
    # Warning: The sample database is very large
    #load_entire_database()

    # Incremental Load
    incremental_load_upsert("customer", "CustomerKey")
    
