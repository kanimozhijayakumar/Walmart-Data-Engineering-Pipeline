#!/bin/bash
set -e

echo "Starting Airflow API server..."
airflow api-server --host 0.0.0.0 --port "${PORT:-10000}" &

sleep 3

echo "Starting DAG processor..."
airflow dag-processor &

echo "Starting scheduler..."
airflow scheduler &

wait -n