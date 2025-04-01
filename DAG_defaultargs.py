from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.operators.dagrun_operator import TriggerDagRunOperator

dag = DAG('dag_defaultargs', description='DAG exemplo de dicionario como defaultargs.', 
            schedule_interval=None, start_date=datetime(2025, 3, 5), catchup=False)

task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)
task2 = TriggerDagRunOperator(task_id="tsk2", trigger_dag_id="dag_called", dag=dag)


task1 >> task2
