"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/incubator-airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.mssql_operator import MsSqlOperator


#MsSqlOperator("SELECT * FROM")

default_args = {
    'owner': 'airflow',
    #'depends_on_past': False,
    'start_date': datetime(2018, 10, 28),
    #'email': ['airflow@example.com'],
    #'email_on_failure': False,
    #'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    dag_id='emir_tutorial_from_airflow', 
    schedule_interval="@daily",
    default_args=default_args)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 3',
    retries=3,
    dag=dag)

templated_command = """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
"""

t3 = BashOperator(
    task_id='templated',
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag)



t4 = BashOperator(
    task_id="create_folder",
    bash_command="""
        dt=`date +%S`
        mkdir "/mnt/c/Users/emirl/Github/airflow/folder_$dt"
        echo "folder_$dt is created"
        echo pwd
        """, 
    dag=dag
)

t2.set_upstream(t1)
t3.set_upstream(t2)
t4.set_upstream(t3)
