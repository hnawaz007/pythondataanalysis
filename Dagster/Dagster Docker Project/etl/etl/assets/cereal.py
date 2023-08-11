"""Collection of Cereal assets"""
import csv
from typing import List

import requests
from dagster import asset, get_dagster_logger

from etl.ops.cereal import CEREAL_URL


@asset
def cereals() -> List[dict]:
    """Example of a Dagster asset represents a list of cereal dicts."""
    response = requests.get(CEREAL_URL, timeout=30)
    lines = response.text.split("\n")
    cereal_list = list(csv.DictReader(lines))
    get_dagster_logger().info(f"Found {len(cereal_list)} cereals")
    return cereal_list


@asset
def highest_calorie_cereal(cereals: List[dict]) -> str:
    """Example of a Dagster asset that represents the highest calorie cereal."""
    sorted_by_calorie = list(sorted(cereals, key=lambda cereal: cereal["calories"]))
    get_dagster_logger().info(
        f'{sorted_by_calorie[-1]["name"]} is the cereal that contains the most calories'
    )
    return sorted_by_calorie[-1]["name"]


@asset
def highest_protein_cereal(cereals: List[dict]) -> str:
    """Example of a Dagster asset that represents the highest protein cereal."""
    sorted_by_protein = list(sorted(cereals, key=lambda cereal: cereal["protein"]))
    get_dagster_logger().info(
        f'{sorted_by_protein[-1]["name"]} is the cereal that contains the most protein'
    )
    return sorted_by_protein[-1]["name"]
