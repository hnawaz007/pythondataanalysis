
from dagster import  asset
from etl.resources.db_conn import get_sql_conn
#import needed libraries
import pandas as pd
import logging


#extract data from sql server
@asset( group_name="TSTpipeline", compute_kind="extraction", io_manager_key="file_io")
def extract_dim_product_category( context) -> pd.DataFrame:
    """Extract from devrep"""
    with get_sql_conn() as conn:
        df = pd.read_sql_query("select * FROM dbo.DimProductCategory", conn)
        context.log.info(df.head())
        return df
    
#load data
@asset( group_name="TSTpipeline", compute_kind="load", io_manager_key="db_io")
def dim_product_category(context, extract_dim_product_category: pd.DataFrame) -> pd.DataFrame:
    """Transform and Load to reporting"""
    try:
        context.log.info(extract_dim_product_category.head())
        df = extract_dim_product_category[['ProductCategoryKey', 'EnglishProductCategoryName']]
        df = df.rename(columns={'EnglishProductCategoryName': 'ProductCategoryName'})
        return df
    except Exception as e:
        context.log.info(str(e))