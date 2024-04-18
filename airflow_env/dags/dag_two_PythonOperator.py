from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.papermill.operators.papermill import PapermillOperator



default_args = {
    'owner': 'coder2j',
    'start_date': datetime(2024, 3, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}



with DAG(
    dag_id='ejecutar_notebook_v1',
    default_args=default_args,
    description='Jupyter Notebook DAG-Test',
    start_date=datetime(2021, 7, 6),
    schedule_interval='@daily'
) as dag:
    task1 = PapermillOperator(
        task_id='ejecutar_notebook_task',
        input_nb='path',
        dag=dag
    )

    task1