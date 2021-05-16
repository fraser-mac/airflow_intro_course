from airflow import DAG

from datetime import datetime

from airflow.operators.bash import BashOperator

default_args = {
    'start_date': datetime(2020, 1, 1)
}

with DAG('parallel_dag', schedule_interval='@daily', default_args=default_args, max_active_runs=1, catchup=True) as dag:
    first_task = BashOperator(
        task_id='first_task',
        bash_command='sleep 3'
    )

    second_task = BashOperator(
        task_id='second_task',
        bash_command='sleep 3'
    )

    third_task = BashOperator(
        task_id='third_task',
        bash_command='sleep 3'
    )

    fourth_task = BashOperator(
        task_id='fourth_task',
        bash_command='sleep 3'
    )    

    first_task >> [second_task, third_task] >> fourth_task 
    