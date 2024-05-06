#import DAG first

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone

# 2. Use BashOperator & PythonOperator
import logging


def _say_hello():
    logging.debun("This is DEBUG log")
    logging.info("hello")

with DAG (
    "hello",
    start_date=timezone.datetime(2024, 5, 6),
    schedule=None,
    tags=["DS525"],
):
    chutimon_start = EmptyOperator(task_id="Chutimon_start")

    echo_hello = BashOperator(
        task_id="echo_hello",
        bash_command="echo 'hello'",
    )

    say_hello = PythonOperator(
        task_id="say_hello",
        python_callable=_say_hello,
    )

    chutimon_end = EmptyOperator(task_id="Chutimon_end")

    chutimon_start >> echo_hello >> chutimon_end
    chutimon_start >> say_hello >> chutimon_end
