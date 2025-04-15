from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable


dag = DAG('dag_variaveis', description='DAG exemplo de utilização de variaveis.', 
            schedule_interval=None, start_date=datetime(2025, 3, 5), catchup=False)


def print_variable(**kwargs):
    minha_var = Variable.get("minhavar")
    print(f'Valor da variavel: {minha_var}')

task1 = PythonOperator(task_id="tsk1", python_callable=print_variable  , dag=dag)

task1