# Airbnb Data Pipeline (Python • Airflow • Docker • PostgreSQL)

A compact, production-style ETL that ingests Airbnb listings (CSV or API), cleans and validates them with pandas, and loads them into a PostgreSQL data warehouse. Orchestrated daily with Apache Airflow.

## 🧩 Airflow DAG in Action

Here’s a snapshot of the **Airbnb Data Pipeline** running successfully in Apache Airflow:

The pipeline runs daily and orchestrates three main tasks:
1. **Extract** – Reads Airbnb listings data (CSV/API)
2. **Transform** – Cleans and enriches data with pandas
3. **Load** – Stores processed data into PostgreSQL warehouse
   
![WhatsApp Image 2025-10-19 at 17 47 10_cacb3bc8](https://github.com/user-attachments/assets/fd92e0c3-7167-4d81-a3da-d15d639de2cf)


## Why this project?
I built this to demonstrate practical **Data Engineering** skills relevant to real teams:
- Containerized orchestration with **Airflow**
- **ETL** with Python (pandas) and **SQLAlchemy**
- **PostgreSQL** data modeling and loading
- Clear, reproducible **Docker Compose** setup


