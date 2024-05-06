#import DAG first

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone

#with open("hello.txt", "w") as f:
#    Chutimon
#    Chutimon
#open file and close file

#DAG IG, Start Date(from package of Airflow), Schedule
# 1. Use EmptyOperator

with DAG (
     "chutimon_dag",
     start_date=timezone.datetime(2024, 5, 6),
     schedule=None,
     tags=["DS525"],

):
     chutimon_first_task = EmptyOperator(task_id="Chutimon_first_task")
     chutimon_second_task = EmptyOperator(task_id="Chutimon_second_task")

     chutimon_first_task >> chutimon_second_task

