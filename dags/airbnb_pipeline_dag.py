from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.bash import BashOperator

# Default DAG args
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Runs daily at 06:00 UTC (you can change)
with DAG(
    dag_id="airbnb_data_pipeline",
    default_args=default_args,
    description="Mini Airbnb ETL to Postgres warehouse",
    schedule="0 6 * * *",           # cron: 06:00 UTC daily
    start_date=datetime(2025, 1, 1),
    catchup=False,
    max_active_runs=1,
    tags=["airbnb", "etl", "demo"],
) as dag:

    # Use BashOperator to run the Python scripts inside the Airflow container
    extract = BashOperator(
        task_id="extract",
        bash_command="python /opt/airflow/scripts/extract.py"
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="python /opt/airflow/scripts/transform.py"
    )

    load = BashOperator(
        task_id="load",
        bash_command="python /opt/airflow/scripts/load.py"
    )

    extract >> transform >> load
