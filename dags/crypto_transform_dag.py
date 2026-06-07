from airflow import DAG 
from airflow.operators.bash import BashOperator 
from datetime import datetime 

default_args = {
    'owner': 'airflow', 
} 

with DAG( 
    dag_id='crypto_transform_pipeline', 
    default_args=default_args, 
    start_date=datetime(2026, 5, 18), 
    schedule_interval='*/1 * * * *', 
    catchup=False
) as dag:

    run_transformation = BashOperator(
        task_id='run_transform_script', 
        bash_command='python /opt/airflow/scripts/transform.py'
    )

    run_transformation
