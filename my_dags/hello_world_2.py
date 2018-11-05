from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator 
from airflow.operators.python_operator import PythonOperator 

def print_hello():
    """ Very simple hello world function """
    return "Hello world, Emir"

def simple_function():
    x = 3
    return(str(x))

dag = DAG(
    "hello_world_2", 
    description="Simple tutorial DAG",
    schedule_interval="* * * * *",
    start_date=datetime(2018, 10, 31), 
    catchup=False)

dummy_operator = DummyOperator(task_id="dummy_task", retries=1, dag=dag)

#hello_operator = PythonOperator(task_id="hello_task", python_callable=print_hello, dag=dag)

simple_operator = PythonOperator(task_id="simple_task", python_callable=simple_function, dag=dag)

# Set up dependencies
dummy_operator >> simple_operator
