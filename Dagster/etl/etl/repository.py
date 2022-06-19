from dagster import repository

from etl.jobs.say_hello import say_hello_job
#
from etl.jobs.run_etl import run_etl_job
from etl.schedules.my_hourly_schedule import my_hourly_schedule
#etl job schedule
from etl.schedules.etl_job_schedule import etl_job_schedule
from etl.sensors.my_sensor import my_sensor


@repository
def etl():
    """
    The repository definition for this etl Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [say_hello_job, run_etl_job]
    schedules = [my_hourly_schedule, etl_job_schedule]
    sensors = [my_sensor]

    return jobs + schedules + sensors
