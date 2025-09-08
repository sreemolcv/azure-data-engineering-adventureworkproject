# Azure Data Engineering Pipeline (AdventureWorks Dataset)

## 📌 Project Overview

This project showcases an end-to-end data engineering solution built on the Azure cloud platform using the AdventureWorks dataset.  
The pipeline follows the **Medallion Architecture (Bronze → Silver → Gold)** to ingest, clean, and transform raw business data into analytics-ready tables for downstream reporting and visualization.

**Goals:**  
- Demonstrate real-world data engineering practices: scalable ingestion, distributed transformations with PySpark, and cloud-based data warehousing using Azure services.

---

## 🏗️ Architecture

**Pipeline Flow:**

- **Azure Blob Storage (Bronze):** Stores raw CSV files from AdventureWorks.
- **Azure Databricks (Silver):** Cleanses, transforms, and standardizes raw data with PySpark.
- **Azure Databricks + Synapse (Gold):** Builds fact/dimension tables in a star schema for BI consumption.
- **Azure Synapse Analytics:** Provides SQL-based reporting and analytics.

---

## ⚙️ Tech Stack

- **Azure Services:** Databricks, Blob Storage, Synapse Analytics
- **Languages:** PySpark, SQL
- **Architecture:** Medallion (Bronze, Silver, Gold)
- **Data Modeling:** Fact & Dimension tables (Star Schema)
- **Tools:** GitHub for versioning, Power BI (optional)

---

## 📂 Repository Structure

```
azure-data-engineering-adventureworks/
│── README.md
│── architecture/
│    └── azure_pipeline_architecture.png
│── notebooks/
│    ├── bronze_ingestion_notebook.ipynb
│    ├── silver_transformation_notebook.ipynb
│    ├── gold_analytics_notebook.ipynb
│── scripts/
│    └── synapse_queries.sql
│── configs/
│    └── connection_config.json   # dummy placeholders only
│── docs/
│    ├── storage_setup.md
│    ├── project_report.md
```

---

## 🔑 Setup Instructions

### 1️⃣ Clone the Repo
```sh
git clone https://github.com/<your-username>/azure-data-engineering-adventureworks.git
cd azure-data-engineering-adventureworks
```

### 2️⃣ Configure Connections
- Update `configs/connection_config.json` with your own Azure credentials.
- A dummy config file with placeholders is included for reference.

### 3️⃣ Run Databricks Notebooks
- Import notebooks from the `notebooks/` folder into Azure Databricks.
- Execute them in order:
  1. Bronze ingestion
  2. Silver transformation
  3. Gold aggregation

### 4️⃣ Execute Synapse Queries
- Run SQL scripts from `scripts/synapse_queries.sql` in Azure Synapse Studio.
- Creates fact/dimension tables for reporting.

---

## 📊 Results

- **Bronze Layer:** Raw AdventureWorks data securely ingested into Blob Storage.
- **Silver Layer:** Standardized & cleansed tables ready for integration.
- **Gold Layer:** Analytics-ready star schema powering Synapse queries and BI dashboards.

---

## 🌟 Key Highlights

- Hands-on implementation of Azure Medallion Architecture.
- Built scalable ETL pipelines using PySpark in Databricks.
- Designed optimized fact/dimension models for analytics in Synapse.
- Demonstrated real-world enterprise practices with cloud-native tools.

---
