from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator 
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
import pandas as pd 
import os 

# Default arguments
default_args = {
    "owner": "emir",
    "depends_on_past": False,
    "start_date": datetime(2018, 10, 20),
    #"email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    "catchup" : False
    # "queue": "bash_queue",
    # "pool": "backfill",
    # "priority_weight": 10,
    # "end_date": datetime(2016, 1, 1),
}

input_directory = '/mnt/c/Users/emirl/Github/airflow/data'
output_directory = '/mnt/c/Users/emirl/Github/airflow/output/test_directory'


def file_read(fpath):
    return("Read file: {}".format(fpath))


def parse_csv_file(file_in, file_out):
    df = pd.read_csv(file_in)
    df["new_col"] = "Hello"
    df.to_csv(file_out, index=False)
    # Print this file to Airflow log
    out_string = "File parsed: {}. Written to: {}".format(file_in, file_out)
    return(out_string)    

# Dag
dag = DAG(
    "emir_learning_apache_airflow", 
    description="Simple tutorial DAG",
    schedule_interval="@daily",
    default_args=default_args)

# Operators
hello_world_bash_operator = BashOperator(
    task_id="bash_hello_world_operator",
    bash_command="echo Hello World",
    dag=dag
)

make_output_directory_bash_operator = BashOperator(
    task_id="make_output_directory",
    #FIXME: Should run even if directory exists
    bash_command="mkdir -p {{ params.output_directory }}",
    params={'output_directory': output_directory},
    #TODO: will the jinja template work even if I use another name than params?
    dag=dag
)

simple_dummy_operator = DummyOperator(task_id="simple_dummy", dag=dag)


parse_csv_file_python_operator = PythonOperator(
    task_id="parse_csv", 
    python_callable=parse_csv_file,
    op_kwargs={
        "file_in" : os.path.join(input_directory, "test.csv"),
        "file_out": os.path.join(output_directory, "out_test.csv")
        },
    dag=dag)


# Set up dependencies
hello_world_bash_operator.set_upstream(simple_dummy_operator)
make_output_directory_bash_operator.set_upstream(hello_world_bash_operator)
parse_csv_file_python_operator.set_upstream(make_output_directory_bash_operator)

