# Walmart Data Engineering Pipeline

An end-to-end Data Engineering project built using **Python, Apache Airflow, dbt, PostgreSQL, Docker, and SQL**.

The pipeline ingests Walmart retail data, orchestrates transformations with Airflow, applies layered dbt models, performs data quality checks, and produces analytics-ready fact and dimension tables.

---

## Architecture

<p align="center">
  <img src="docs/walmart-data-engineering-architecture.png"
       width="100%">
</p>

---

## Tech Stack

- Python
- SQL
- PostgreSQL
- Apache Airflow
- dbt Core
- Docker
- GitHub
- Render

---

## Pipeline Flow

```text
Walmart CSV Data
      ↓
Python Ingestion
      ↓
PostgreSQL Raw Layer
      ↓
Apache Airflow
      ↓
dbt Source Freshness
      ↓
Silver Technical Layer
      ↓
dbt Tests
      ↓
Silver Business Layer
      ↓
Gold Dimensions
      ↓
Gold Fact Table
      ↓
Analytics-Ready Data
```

---

## Data Architecture

The PostgreSQL environment is organized into multiple layers:

```text
public      → Raw source data
silver_t    → Technical transformations
silver_b    → Business transformations
gold        → Analytics-ready models
```

### Gold Models

```text
gold.dim_customers
gold.dim_employees
gold.dim_orders
gold.dim_products
gold.dim_stores
gold.fact_orders
```

Final fact table:

```text
gold.fact_orders
```

Current row count:

```text
300,513
```

---

## Airflow Orchestration

Main DAG:

```text
orchestrate
```

Execution flow:

```text
ingest_cdc
   ↓
clean_target
   ↓
source_freshness
   ↓
silver_technical
   ↓
silver_technical_tests
   ↓
silver_business
   ↓
silver_business_tests
   ↓
gold_dimensions
   ↓
gold_facts
```

Airflow manages task dependencies and ensures downstream processing runs only after successful upstream execution.

---

## Data Quality

Data quality checks are integrated into the pipeline using dbt.

The project includes:

- Source freshness checks
- dbt model tests
- Null validation
- Uniqueness checks
- Relationship validation

This helps prevent invalid data from reaching the Gold layer.

---

## Project Structure

```text
Walmart-Data-Engineering-Pipeline/
│
├── airflow_dbt_project/
│   ├── dags/
│   ├── config/
│   ├── walmart_project/
│   │   ├── models/
│   │   └── snapshots/
│   ├── Dockerfile
│   └── docker-compose.yaml
│
├── walmart_dataset/
│   ├── data/
│   ├── ddl/
│   └── load_data.py
│
├── docs/
│   └── walmart-data-engineering-architecture.png
│
├── render.yaml
└── README.md
```

---

## Run Locally

Clone the repository:

```bash
git clone https://github.com/kanimozhijayakumar/Walmart-Data-Engineering-Pipeline.git
cd Walmart-Data-Engineering-Pipeline
```

Create the PostgreSQL database:

```bash
createdb walmart_db
psql walmart_db < walmart_dataset/ddl/walmart_schema.sql
```

Load the source data:

```bash
python3 walmart_dataset/load_data.py
```

Start Airflow:

```bash
cd airflow_dbt_project
docker compose up -d
```

Open Airflow:

```text
http://localhost:8080
```

---

## Key Engineering Concepts

This project demonstrates:

- End-to-end ETL / ELT pipeline design
- Apache Airflow orchestration
- dbt transformations
- Layered data architecture
- Data quality validation
- Dimensional modeling
- Fact and dimension tables
- PostgreSQL warehousing
- Dockerized environments
- Cloud deployment concepts

---


**Kanimozhi J**

Data Engineering
