# 🏠 Airbnb Data Pipeline (Python • Airflow • Docker • PostgreSQL)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-orange?logo=apacheairflow&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white)
![Build Status](https://img.shields.io/badge/Status-Stable-success)
![License](https://img.shields.io/badge/License-MIT-green)

A **production-style ETL pipeline** designed to automate the ingestion, transformation, and loading of Airbnb listings data into a PostgreSQL data warehouse.  
The workflow is fully **containerized with Docker** and orchestrated using **Apache Airflow** for daily scheduling and monitoring.

---

## ⚙️ Project Overview

The **Airbnb Data Pipeline** automates the following key processes:

1. **Extract** – Ingests Airbnb listings from CSV files or a public API  
2. **Transform** – Cleans, enriches, and validates the data using **pandas**  
3. **Load** – Loads the processed data into a **PostgreSQL** warehouse using **SQLAlchemy**

This setup demonstrates how to design a modular, scalable, and reproducible ETL process suitable for real-world data engineering environments.

---

## 🚀 Technologies Used

- **Python** – Data manipulation, validation, and scripting  
- **Apache Airflow** – Workflow orchestration and task scheduling  
- **PostgreSQL** – Centralized data storage and modeling  
- **SQLAlchemy** – ORM for efficient database interaction  
- **Docker & Docker Compose** – Containerization for portability and consistency  

---

## 📊 Airflow DAG in Action

Below is a snapshot of the pipeline running in **Apache Airflow**, showing the three core ETL tasks executed in sequence:

![Airbnb DAG Screenshot](https://github.com/user-attachments/assets/fd92e0c3-7167-4d81-a3da-d15d639de2cf)

Each DAG run performs:
- **Extract:** Fetch raw Airbnb data  
- **Transform:** Apply cleaning and enrichment logic  
- **Load:** Store refined data in PostgreSQL  

---

## 🎯 Purpose & Key Takeaways

This project highlights hands-on experience with modern **Data Engineering** practices, including:
- Workflow automation using **Airflow DAGs**  
- Data extraction and cleaning with **pandas**  
- Data modeling and loading into **PostgreSQL**  
- Deployment via **Docker Compose** for easy reproducibility  

It serves as a demonstration of building a **scalable, maintainable ETL pipeline** from scratch — a valuable foundation for production-grade data workflows.

---

## 🧠 Future Improvements

- Add data quality validation with **Great Expectations**  
- Integrate automated logging and alerting  
- Extend to real-time ingestion using **Kafka** or **Spark Streaming**

---
