from dagster import asset, get_dagster_logger, AssetExecutionContext, AssetSpec, AssetKey
from ..resources import DltResource
from ..dlt import get_data


@asset(group_name="database_assets", compute_kind="postgres")
def fx_pipeline(context: AssetExecutionContext, pipeline: DltResource):
    """load fx rate api data to fx_table in postgres"""
    logger = get_dagster_logger()
    results = pipeline.create_pipeline(get_data, table_name='fx_table')
    logger.info(results)