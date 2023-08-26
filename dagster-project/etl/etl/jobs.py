
from etl import assets_dataanalysis
from dagster import (
    define_asset_job,
    AssetSelection
)

# define jobs as selections over the larger graph
run_jupyter_job = define_asset_job("run_jupyter_job", AssetSelection.groups("Notebooks"))
