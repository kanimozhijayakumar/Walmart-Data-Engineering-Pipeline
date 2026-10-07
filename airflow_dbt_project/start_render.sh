#!/bin/bash
set -e

echo "Running Airflow DB migration..."
airflow db migrate

echo "Starting Airflow API server..."
airflow api-server --host 0.0.0.0 --port "${PORT:-10000}" &

echo "Starting DAG processor..."
airflow dag-processor &

echo "Starting scheduler..."
airflow scheduler &

wait -n