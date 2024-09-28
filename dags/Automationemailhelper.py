from datetime import datetime
from airflow.models import DAG,Variable
from airflow.operators.python_operator import PythonOperator
from bots.emailhelper import send


default_args={

    "owner":"j",
    "start_date":datetime(2024,9,27)
}
with DAG(
    dag_id="Automationemailhelper",
    default_args=default_args,
    schedule_interval=None) as dag:
    
    send_email=PythonOperator(
    task_id="send_email",
    python_callable=send
    )
    send_email