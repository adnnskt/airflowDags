from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG('trigger_dag', description='DAG exemplo de utilização de trigger em nivel de task', 
            schedule_interval=None, start_date=datetime(2025, 3, 5), catchup=False)

task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag
                     , trigger_rule='one_failed')


[task1, task2] >> task3 #Formato em precedência