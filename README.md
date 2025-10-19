# Airbnb Data Pipeline (Python • Airflow • Docker • PostgreSQL)

A compact, production-style ETL that ingests Airbnb listings (CSV or API), cleans and validates them with pandas, and loads them into a PostgreSQL data warehouse. Orchestrated daily with Apache Airflow.

## 🧩 Airflow DAG in Action

Here’s a snapshot of the **Airbnb Data Pipeline** running successfully in Apache Airflow:

The pipeline runs daily and orchestrates three main tasks:
1. **Extract** – Reads Airbnb listings data (CSV/API)
2. **Transform** – Cleans and enriches data with pandas
3. **Load** – Stores processed data into PostgreSQL warehouse


## Why this project?
I built this to demonstrate practical **Data Engineering** skills relevant to real teams:
- Containerized orchestration with **Airflow**
- **ETL** with Python (pandas) and **SQLAlchemy**
- **PostgreSQL** data modeling and loading
- Clear, reproducible **Docker Compose** setup

## Architecture
