from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
import random
from datetime import datetime


dag = DAG('dag_branch', description='DAG exemplo de utilização de branch.', 
            schedule_interval=None, start_date=datetime(2025, 3, 5), catchup=False)


def gera_numero_aleatorio():
    return random.randint(1, 100)

gera_numero_aleatorio_task = PythonOperator(
    task_id='gera_numero_aleatorio_task',
    python_callable = gera_numero_aleatorio, dag=dag)

def avalia_numero_aleatorio(**context):
    number = context['task_instance'].xcom_pull(task_ids='gera_numero_aleatorio_task')
    if number % 2 == 0:
        return 'task1'
    else:
        return 'task2'

branch_task = BranchPythonOperator(
    task_id="branch_task",
    python_callable=avalia_numero_aleatorio,
    provide_context=True,
    dag=dag
)

task1 = BashOperator(task_id="tsk1", bash_command='echo "Número Par"', dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command='echo "Número Impar"', dag=dag)

gera_numero_aleatorio_task >> branch_task
branch_task >> task1
branch_task >> task2