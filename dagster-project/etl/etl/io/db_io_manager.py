import json

import pandas as pd
from sqlalchemy import create_engine

from dagster import (
    Field,
    IOManager,
    InitResourceContext,
    InputContext,
    OutputContext,
    StringSource,
    io_manager,
)

class PostgresDataframeIOManager(IOManager):
    def __init__(self, uid: str, pwd: str, server: str, db: str, port: str) -> None:
        # credentials passed to IO Manager 
        self.uid = uid
        self.pwd = pwd
        self.db = db
        self.server = server
        self.port = port

    def handle_output(self, context: OutputContext, obj: pd.DataFrame):
        # Skip handling if the output is None
        if obj is None:
            return

        table_name = context.asset_key.to_python_identifier()
        #
        engine = create_engine(f'postgresql://{self.uid}:{self.pwd}@{self.server}:{self.port}/{self.db}')
        #
        obj.to_sql(table_name, engine, if_exists='replace', index=False)
        
        # Recording metadata from an I/O manager:
        # https://docs.dagster.io/concepts/io-management/io-managers#recording-metadata-from-an-io-manager
        context.add_output_metadata({"db": self.db, "table_name": table_name})

    def load_input(self, context: InputContext):
        # upstream_output.asset_key is the asset key given to the Out that we're loading for
        table_name = context.upstream_output.asset_key.to_python_identifier()
        #
        engine = create_engine(f'postgresql://{self.uid}:{self.pwd}@{self.server}:{self.port}/{self.db}')
        df = pd.read_sql( f"SELECT * FROM public.{table_name}", engine)
        return df


@io_manager(
    config_schema={
        "uid": StringSource,
		"pwd": StringSource,
        "server": StringSource,
        "db":StringSource,
		"port":StringSource,
    }
)
def postgres_pandas_io_manager(init_context: InitResourceContext) -> PostgresDataframeIOManager:
    return PostgresDataframeIOManager(
        pwd=init_context.resource_config["pwd"],
        uid=init_context.resource_config["uid"],
        server=init_context.resource_config["server"],
		db=init_context.resource_config["db"],
		port=init_context.resource_config["port"],
    )
