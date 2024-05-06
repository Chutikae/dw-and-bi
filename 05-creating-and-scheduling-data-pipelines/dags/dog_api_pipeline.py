#import DAG first

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone


import requests
import json


def _get_dog_api():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    logging.info(data)
    with open("/opt/airflow/dags/dog.json", "w") as f:
        json.dump(data, f)

with DAG (
    "dog_api_pipeline",
    start_date=timezone.datetime(2024, 5, 6),
    schedule="@daily", # Cron expression
    tags=["DS525"],
):
    chutimon_start = EmptyOperator(task_id="Chutimon_start")

    get_dog_api = PythonOperator(
        task_id="get_dog_api",
        python_callable=_get_dog_api,
    )

    chutimon_end = EmptyOperator(task_id="Chutimon_end")

    chutimon_start >> get_dog_api >> chutimon_end

