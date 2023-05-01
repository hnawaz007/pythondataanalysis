from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
#
from airflow import DAG




default_args = {
    "owner": "Airflow",
    "start_date": datetime(2022, 8, 21),
    'email': ['admin@localmail.com'],
    'email_on_failure': True,
}

with DAG(dag_id="test_mail",
        schedule_interval="@once",
        default_args=default_args,
    ) as dag:

    test_email = EmailOperator(
       task_id='email_test',
       to='hnawaz@localmail.com',
       subject='Airflow Alert !!!',
       html_content="""<h1>Testing Email using Airflow</h1>""",
    )
    
test_email