# Creating and Scheduling Data Pipelines

Name : Chutimon Cherdpongtagit
ID : 66199160146

- The main point of this project is Airflow. (especially Apache Airflow)
- Focus on 'LocalExecutor' (no worker as the main point with less results when coapares to Celery Executor)


Additional knowledges of the contents for running Airflow with CeleryExecutor. 
(* no use in this project except for airflow-init.)
1. airflow-scheduler - The scheduler monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.
2. airflow-webserver - The webserver is available at http://localhost:8080.
3. airflow-worker - The worker that executes the tasks given by the scheduler.
4. airflow-triggerer - The triggerer runs an event loop for deferrable tasks.
5. airflow-init - The initialization service.
6. postgres - The database.
7. redis - The redis - broker that forwards messages from scheduler to worker.
Optionally, you can enable flower by adding --profile flower option, e.g. docker compose --profile flower up, or by explicitly specifying it on the command line e.g. docker compose up flower.
8. flower - The flower app for monitoring the environment. It is available at http://localhost:5555.

Step for doing this project

1. Fetching docker-compose.yaml

To deploy Airflow on Docker Compose by using the code:

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.1/docker-compose.yaml'

2. Setting the right Airflow user

 to know your host user id and needs to have group id,
 and configure for the docker-compose by using the code:

mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env

3. docker compose up to running the edited docker-composed.yaml
4. Check the port 8080 to open the login site of Airflow
5. Sign in with the given username and password from this code at below :
      _AIRFLOW_WWW_USER_USERNAME: ${_AIRFLOW_WWW_USER_USERNAME:-airflow}
      _AIRFLOW_WWW_USER_PASSWORD: ${_AIRFLOW_WWW_USER_PASSWORD:-airflow}
6. Find example_complex from DAGs - Airflow website:
       https://fictional-space-happiness-7vvqxvr797v4cwp4x-8080.app.github.dev/home

7. Check example_complex and trigger DAG , then enter it to observe the details such as the relationship of entity in graph

8. Back to Codespace in Guthub -> Create new file at dags as 'chutimon_dag.py'
9. Code in 'chutimon_dag.py' (the result is shown in image folder)

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils import timezone

10. Code in 'hello.py' (the result is shown in image folder)

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone

11. Apply with your own demo (use dog API) - Problem : There is some error I cannot figure out.
So, the json file isn't automatically upload on codespace.