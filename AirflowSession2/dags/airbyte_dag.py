from airflow import DAG
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.airbyte.sensors.airbyte import AirbyteJobSensor
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.utils.trigger_rule import TriggerRule
import pendulum
from airflow.models import Variable

#get password from environmnet var
AIRBYTE_CONNECTION_ID = Variable.get("AIRBYTE_CONNECTION_ID")

with DAG(dag_id='airbyte_sync_airflow_dag',
        default_args={'owner': 'airflow'},
        schedule='@daily',
        start_date=pendulum.today('UTC').add(days=-1),
        template_searchpath=["/opt/sql/"] 
   ) as dag:

   trigger_airbyte_sync = AirbyteTriggerSyncOperator(
       task_id='airbyte_trigger_sync',
       airbyte_conn_id='airbyte',
       connection_id=AIRBYTE_CONNECTION_ID,
       asynchronous=True,
        email_on_failure=True,
        email='airflow@localmail.com',
   )

   wait_for_sync_completion = AirbyteJobSensor(
       task_id='airbyte_check_sync',
       airbyte_conn_id='airbyte',
       airbyte_job_id=trigger_airbyte_sync.output,
        email_on_failure=True,
        email='airflow@localmail.com',
   )

   merge_product = PostgresOperator(
        task_id='merge_product',
        postgres_conn_id='postgres',
        sql='/denornamlized_product.sql',
        retries = 2,
        email_on_failure=True,
        email='hnawaz@localmail.com',
   )

   trigger_airbyte_sync >> wait_for_sync_completion >> merge_product 