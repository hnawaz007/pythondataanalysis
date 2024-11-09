from dagster import Definitions, load_assets_from_modules

from fx_rate import assets  # noqa: TID252

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)
