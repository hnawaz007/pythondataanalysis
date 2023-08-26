from dagster import ScheduleDefinition
from etl.jobs import run_jupyter_job


every_weekday_9am = ScheduleDefinition(
    job=run_jupyter_job,
    cron_schedule="0 9 * * 1-5",
    execution_timezone="America/New_York",
)