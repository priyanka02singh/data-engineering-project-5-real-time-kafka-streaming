# ⚡ Project 5: Real-Time Kafka Streaming Pipeline

## 📌 Overview

This project implements a real-time streaming data pipeline inspired by Kafka architecture.
It simulates event-driven data processing using Python producers, consumers, and transformation logic,
combined with Airflow for orchestration and monitoring. 
The system demonstrates how real-time data flows through a streaming architecture used in modern data platforms.

---

## 🏗️ System Architecture
```text

Crypto Event Source
        ↓
Producer (scripts/producer.py)
        ↓
Message Stream (Kafka-like simulation)
        ↓
Consumer (scripts/consumer.py)
        ↓
Transformation Layer (scripts/transform.py)
        ↓
Database Layer (PostgreSQL / SQLite)
        ↓
Airflow DAG Orchestration (dags/crypto_transform_dag.py)

```
---

## ⚙️ Core Components

### 📤 1. Producer Layer

- Generates real-time crypto market events
- Simulates streaming data ingestion
- Pushes events into message stream

### 📥 2. Consumer Layer

- Reads streaming events
- Processes incoming data in real-time
- Prepares data for transformation
  
### 🔄 3. Transformation Layer

- Cleans and structures streaming data
- Applies business logic to events
- Prepares analytics-ready output
  
### 🧠 4. Orchestration Layer (Airflow)

- Schedules and monitors pipeline execution
- Ensures workflow reliability
- Manages DAG dependencies

---

##  🧰 Tech Stack

- Python (Streaming Logic)
- Apache Airflow (Orchestration)
- Docker (Containerization)
- SQL (Data Storage)
- Kafka-style Event Simulation

---
  
## 🔄 Pipeline Flow

Producer → Stream → Consumer → Transform → Database → Airflow DAG

---
## 🚀 Execution Modes

### ▶ Manual Mode
```bash
python scripts/producer.py
python scripts/consumer.py
python scripts/transform.py
```
### ▶ Airflow Mode
```bash
Triggered via DAG:
dags/crypto_transform_dag.py
```
---

## 📁 Project Structure
```text
scripts/
  ├── producer.py
  ├── consumer.py
  ├── transform.py

dags/
  ├── crypto_transform_dag.py

docker-compose.yml
requirements.txt
README.md
```
---

## 🧠 Key Engineering Highlights

- Event-driven architecture simulation
- Streaming pipeline design (Kafka-style)
- Modular Python micro-components
- Airflow-based orchestration
- Production-style workflow structure

---

## 🚀 Outcome

This project demonstrates a real-time data streaming pipeline that mimics Kafka-based architectures
used in modern fintech and analytics systems.

It bridges the gap between batch ETL systems and real-time event processing systems.
