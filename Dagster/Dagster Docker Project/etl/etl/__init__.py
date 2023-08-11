"""Definitions that provide Dagster code locations."""
from dagster import Definitions

from etl.assets.cereal import cereals, highest_calorie_cereal, highest_protein_cereal
from etl.jobs import complex_job, hello_cereal_job
from etl.schedules import every_weekday_9am

defs = Definitions(
    assets=[cereals, highest_calorie_cereal, highest_protein_cereal],
    jobs=[complex_job, hello_cereal_job],
    schedules=[every_weekday_9am],
)
