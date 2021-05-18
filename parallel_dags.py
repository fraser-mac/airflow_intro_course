from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.task_group import TaskGroup

from subdags.subdag_parallel_dag import subdag_parallel_dag
from datetime import datetime



default_args = {
    'start_date': datetime(2020, 1, 1)
}

with DAG('parallel_dag', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    first_task = BashOperator(
        task_id='first_task',
        bash_command='sleep 3'
    )

    with TaskGroup('processing_tasks') as processing_tasks:
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

    first_task >> processing_tasks >> fourth_task 
    
