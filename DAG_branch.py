from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import airflow.operators.python_operator as PythonOperator
import airflow.operators.branch_operator as BranchOperator
import random
from datetime import datetime


dag = DAG('dag_branch', description='DAG exemplo de utilização de branch.', 
            schedule_interval=None, start_date=datetime(2025, 3, 5), catchup=False)


def gera_numero_aleatorio():
    return random.randint(1, 100)

task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag, pool="mypool")
task2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag, pool="mypool", priority_weight=5)
task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag, pool="mypool")
task4 = BashOperator(task_id="tsk4", bash_command="sleep 5", dag=dag, pool="mypool", priority_weight=10)

