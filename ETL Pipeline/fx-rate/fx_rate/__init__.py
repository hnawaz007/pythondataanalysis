
from dagster import Definitions, load_assets_from_modules, define_asset_job, ScheduleDefinition

from . import assets
from .resources import DltResource

all_assets = load_assets_from_modules([assets])

fx_job = define_asset_job(name="api_to_postgres", selection= ['fx_pipeline'])

fx_job_schedule = ScheduleDefinition(
    job=fx_job, cron_schedule="0 9 * * *", execution_timezone="America/New_York"
)

defs = Definitions(
    assets=all_assets,
    jobs=[fx_job],
    schedules=[fx_job_schedule],
    resources={
        "pipeline": DltResource(
            pipeline_name = "api_to_postgres",
            dataset_name = "incremental",
            destination = "postgres",
        ),
    }
)