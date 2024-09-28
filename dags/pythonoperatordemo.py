from datetime import datetime
from airflow.models import DAG, Variable
from airflow.operators.python_operator import PythonOperator
from bots.python_helper import call


default_args={
    'owner':'J',
    'start_date': datetime(2022,6,9)

}

with DAG(
    
    dag_id="pythonoperatordemo1",
    default_args=default_args,
    schedule_interval=None)as dag:
    
    start_dag=PythonOperator(
        task_id='start_dag',
        python_callable=call
    )

    start_dag