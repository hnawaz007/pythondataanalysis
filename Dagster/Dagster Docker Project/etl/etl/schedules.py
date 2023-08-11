"""Collection of Cereal schedules"""

from dagster import schedule

from etl.jobs import complex_job


# https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules
@schedule(
    cron_schedule="0 9 * * 1-5",
    job=complex_job,
    execution_timezone="Europe/Stockholm",
)
def every_weekday_9am(context):
    """Example of how to setup a weekday schedule for a job."""
    date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    return {"ops": {"download_cereals": {"config": {"date": date}}}}
