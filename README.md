# Retail ETL Pipeline

## Overview

Retail ETL Pipeline is an end-to-end Data Engineering project built with Python, Pandas, and PostgreSQL. The pipeline extracts retail data from CSV files, validates and transforms it, and loads the cleaned data into a PostgreSQL database.

The project demonstrates the complete ETL (Extract, Transform, Load) workflow along with data validation, logging, environment variable management, and relational database design.

---

## Features

* Extract data from multiple CSV files
* Validate data quality

  * Missing values
  * Duplicate rows
  * Duplicate primary keys
  * Email validation
  * Phone number validation
  * Schema validation
* Transform data

  * Trim whitespace
  * Standardize text case
  * Convert data types
  * Save cleaned CSV files
* Load cleaned data into PostgreSQL
* Logging using Python's logging module
* Environment variable support using `.env`
* SQL scripts for creating, truncating, and dropping tables

---

## Tech Stack

* Python
* Pandas
* PostgreSQL
* psycopg2
* python-dotenv
* Git & GitHub

---

## Project Structure

```text
Retail-ETL-Pipeline/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── logs/
│   └── etl.log
│
├── sql/
│   ├── create_tables.sql
│   ├── truncate_tables.sql
│   └── drop_tables.sql
│
├── src/
│   ├── config/
│   ├── extract/
│   ├── validate/
│   ├── transform/
│   └── load/
│
├── .env.example
├── requirements.txt
├── main.py
└── README.md
```

---

## ARCHITECTURE DIAGRAM

CSV Files
     │
     ▼
Extract
     │
     ▼
Validation
     │
     ▼
Transformation
     │
     ▼
PostgreSQL

## ETL Workflow

```text
Raw CSV Files
       │
       ▼
Extract
       │
       ▼
Validation
       │
       ▼
Transformation
       │
       ▼
Cleaned CSV Files
       │
       ▼
Load
       │
       ▼
PostgreSQL Database
```

---

## Database Tables

* customers
* products
* orders
* order_items
* payments

The database is designed using primary and foreign key relationships to maintain referential integrity.

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd retail-etl-pipeline
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file using `.env.example` and update it with your PostgreSQL credentials.

Example:

```text
DB_HOST=localhost
DB_NAME=retail_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
```

### 4. Create the database

Create a PostgreSQL database named:

```text
retail_db
```

### 5. Create the tables

```bash
psql -U postgres -d retail_db -f sql/create_tables.sql
```

### 6. Run the ETL Pipeline

```bash
python main.py
```

---

## Output

After execution, the pipeline will:

* Read raw CSV files
* Validate the datasets
* Clean and transform the data
* Save cleaned CSV files
* Load the cleaned data into PostgreSQL
* Generate ETL logs

---

## Future Improvements

* Apache Spark integration
* Apache Airflow workflow orchestration
* Docker support
* AWS S3 integration
* Data warehouse integration
* Automated testing
* CI/CD pipeline
* Incremental loading
* Data quality dashboard

---

## Author

**Lucky Jha**

Aspiring Data Engineer passionate about building scalable data pipelines and solving real-world data engineering problems.
