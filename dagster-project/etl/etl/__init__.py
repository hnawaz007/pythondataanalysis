from dagster import Definitions, load_assets_from_modules
from dagstermill import local_output_notebook_io_manager

from . import assets_productcategory, assets_dataanalysis
from .io import file_io, db_io_manager
from etl.jobs import run_jupyter_job
from etl.schedules import every_weekday_9am

all_assets = load_assets_from_modules([assets_productcategory, assets_dataanalysis])

defs = Definitions(
    assets=all_assets,
    jobs=[run_jupyter_job],
    schedules=[every_weekday_9am],
    resources={
        "file_io": file_io.LocalFileSystemIOManager(),
         "output_notebook_io_manager": local_output_notebook_io_manager,
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
