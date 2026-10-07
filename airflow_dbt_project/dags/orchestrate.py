from airflow.sdk import dag, task
from airflow.operators.bash import BashOperator


@dag
def orchestrate():

    @task
    def ingest_cdc():
        print("CDC ingestion skipped for local demo")
        return "CDC Ingestion Completed"

    @task.bash
    def clean_target():
        return (
            "rm -rf /opt/airflow/walmart_project/target && "
            "rm -rf /opt/airflow/walmart_project/logs"
        )

    @task.bash
    def source_freshness():
        return "cd /opt/airflow/walmart_project && dbt source freshness"

    silver_technical = BashOperator(
        task_id="silver_technical",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt run --select silver_t",
    )

    silver_technical_tests = BashOperator(
        task_id="silver_technical_tests",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt test --select silver_t",
    )

    silver_business = BashOperator(
        task_id="silver_business",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt run --select silver_b",
    )

    silver_business_tests = BashOperator(
        task_id="silver_business_tests",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt test --select silver_b",
    )

    gold_ephermeral = BashOperator(
        task_id="gold_ephermeral",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt run --select gold/ephermeral",
    )

    gold_dimensions = BashOperator(
        task_id="gold_dimensions",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt snapshot",
    )

    gold_facts = BashOperator(
        task_id="gold_facts",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt run --select fact_orders",
    )

    (
        ingest_cdc()
        >> clean_target()
        >> source_freshness()
        >> silver_technical
        >> silver_technical_tests
        >> silver_business
        >> silver_business_tests
        >> gold_ephermeral
        >> gold_dimensions
        >> gold_facts
    )


orchestrate_dag = orchestrate()