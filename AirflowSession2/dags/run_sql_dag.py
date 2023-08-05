from datetime import datetime
from airflow import DAG, task
from airflow.providers.postgres.operators.postgres import PostgresOperator



default_args = {
    "owner": "hnawaz",
    "start_date": datetime(2023, 6, 7),
    'email': ['hnawaz@localmail.com'],
    'email_on_failure': True,
    'retries': 1,

}


with DAG(dag_id='products_dim_denormalized',
         default_args=default_args,
         schedule_interval="@once",
         catchup=False,
         template_searchpath='/opt/sql/',
         tags=['etl', 'analytics', 'product']) as dag:


    join_products_tables = PostgresOperator(
        task_id='join_products_tables',
        postgres_conn_id='postgres',
        sql='dimproduct.sql'
    )

    join_products_tables