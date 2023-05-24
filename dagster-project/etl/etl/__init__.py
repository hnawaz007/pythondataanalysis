from dagster import Definitions, load_assets_from_modules

from . import assets_productcategory
from .io import file_io, db_io_manager

all_assets = load_assets_from_modules([assets_productcategory])

defs = Definitions(
    assets=all_assets,
    resources={
        "file_io": file_io.LocalFileSystemIOManager(),
        "db_io": db_io_manager.postgres_pandas_io_manager.configured(
                {
                "server": {"env": "server"},
                "db": {"env": "db"},
                "uid": {"env": "uid"},
                "pwd": {"env": "pwd"},
                "port": {"env": "port"},
            }
         ),

    }
)
