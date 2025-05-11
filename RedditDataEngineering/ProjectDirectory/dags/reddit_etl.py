from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import importlib.util
import sys
from pathlib import Path

# Dynamically import scripts/extract_reddit.py
extract_path = str(Path(__file__).resolve().parent.parent / 'scripts' / 'extract_reddit.py')
load_path = str(Path(__file__).resolve().parent.parent / 'scripts' / 'load_to_postgres.py')
upload_path = str(Path(__file__).resolve().parent.parent / 'scripts' / 'upload_to_s3.py')

def import_function_from_file(filepath, func_name):
    spec = importlib.util.spec_from_file_location(func_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, func_name)

extract_reddit_data = import_function_from_file(extract_path, 'extract_reddit_data')
load_to_postgres = import_function_from_file(load_path, 'load_to_postgres')
upload_to_s3 = import_function_from_file(upload_path, 'upload_to_s3')

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'reddit_etl',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
)

t1 = PythonOperator(
    task_id='extract_reddit',
    python_callable=extract_reddit_data,
    dag=dag
)
t2 = PythonOperator(
    task_id='load_to_postgres',
    python_callable=load_to_postgres,
    dag=dag
)
t3 = PythonOperator(
    task_id='upload_to_s3',
    python_callable=upload_to_s3,
    dag=dag
)

t1 >> t2 >> t3 