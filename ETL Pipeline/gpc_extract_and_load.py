import time
from datetime import datetime
from airflow.decorators import dag, task
from airflow.providers.microsoft.mssql.hooks.mssql import MsSqlHook
import pandas as pd
from google.oauth2 import service_account

# Declare Dag
@dag(schedule_interval="0 10 * * *", start_date=datetime(2022, 2, 15), catchup=False, tags=['load_gcp'])
# Define Dag Function
def extract_and_load():
# Define tasks
    @task()
    def sql_extract():
        try:
            hook = MsSqlHook(mssql_conn_id="sqlserver")
            sql = """ select  t.name as table_name  
            from sys.tables t where t.name in ('DimSalesTerritory') """
            df = hook.get_pandas_df(sql)
            # print(df.head())
            print(df)
            tbl_dict = df.to_dict('dict')
            return tbl_dict
        except Exception as e:
            print("Data extract error: " + str(e))
    #
    @task()
    def gcp_load(tbl_dict: dict):
        #
        try:
            credentials = service_account.Credentials.from_service_account_file( '/home/airflow/dotted-music-357620-02b4a53537b7.json')
            project_id = "your-gcp-account-id"
            dateset_ref = "AdventureWorks"
            # 
            for value in tbl_dict.values():
                #print(value)
                val = value.values()
                for v in val:
                    #print(v)
                    rows_imported = 0
                    sql = f'select * FROM {v}'
                    hook = MsSqlHook(mssql_conn_id="sqlserver")
                    df = hook.get_pandas_df(sql)
                    print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {v} ')
                    df.to_gbq( destination_table=f'{dateset_ref}.src_{v}',  project_id=project_id, credentials=credentials, if_exists="replace" )
                    rows_imported += len(df)
        except Exception as e:
            print("Data load error: " + str(e))
    # call task functions
    tbl_dict = sql_extract()
    tbl_summary = gcp_load(tbl_dict)
#
gcp_extract_and_load = extract_and_load()
