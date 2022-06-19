from dagster import schedule

from etl.jobs.run_etl import run_etl_job


@schedule(cron_schedule="0 10 * * *", job=run_etl_job, execution_timezone="US/Central")
def etl_job_schedule(_context):
    run_config = {}
    return run_config
