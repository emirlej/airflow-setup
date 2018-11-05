from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator 
from airflow.operators.python_operator import PythonOperator 

def print_hello():
    """ Very simple hello world function """
    return "Hello world"

dag = DAG(
    "hello_world", 
    description="Simple tutorial DAG",
    schedule_interval="0 * * * *",
    start_date=datetime(2018, 10, 31), 
    catchup=False)

dummy_operator = DummyOperator(task_id="dummy_task", retries=3, dag=dag)

hello_operator = PythonOperator(task_id="hello_task", python_callable=print_hello, dag=dag)

# Set up dependencies
dummy_operator >> hello_operator
