from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


dag = DAG('dag_xcom', description='DAG exemplo de utilização do xcom.', 
            schedule_interval=None, start_date=datetime(2025, 3, 5), catchup=False)


def task_write(**kwargs):
    ti = kwargs['ti']
    ti.xcom_push(key='valorxcom1', value=10200)
    

task1 = PythonOperator(task_id="tsk1", python_callable=task_write  , dag=dag)

def task_read(**kwargs):
    ti = kwargs['ti']
    valor = ti.xcom_pull(key='valorxcom1')
    print(f'Valor do xcom: {valor}')


task2 = PythonOperator(task_id="tsk2", python_callable=task_read, dag=dag)

task1 >> task2
