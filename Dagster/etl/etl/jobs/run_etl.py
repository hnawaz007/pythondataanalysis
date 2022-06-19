from dagster import job, op

from etl.ops.etl import extract_dim_product_category, load_dim_product_category

@job
def run_etl_job():
    """
    A job definition. This example job has a single op.

    For more hints on writing Dagster jobs, see our documentation overview on Jobs:
    https://docs.dagster.io/concepts/ops-jobs-graphs/jobs-graphs
    """
    df, tbl = extract_dim_product_category()
    load_dim_product_category(df,tbl)
