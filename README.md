# ⚡ Project 5: Real-Time Streaming Data Pipeline using Apache Kafka

## 📌 Overview

This project simulates a real-time event-driven data pipeline that processes continuous streams of events using Apache Kafka. The system demonstrates how modern data platforms handle high-throughput, real-time data ingestion, processing, and downstream consumption for analytics use cases.

The pipeline is designed to mimic real-world streaming systems used in domains such as fintech, e-commerce, and real-time monitoring platforms.

---
## 🎯 Business Problem

Modern systems generate continuous streams of data such as:

- financial transactions (trades, payments)
- user activity events (clicks, purchases, views)
- system monitoring logs (latency, errors, usage spikes)

Traditional batch pipelines cannot process this data with low latency.

### This project solves:
- How to ingest high-throughput event streams reliably
- How to decouple producers and consumers using Kafka
- How to process streaming data in real time
- How to detect anomalies and generate alerts
- How to route processed data to downstream analytics systems

---

## 🏗️ System Architecture
```text

        ┌────────────────────┐
        │  Event Producers   │
        └─────────┬──────────┘
                  │
     ┌────────────▼──────────────────────┐
     │        Kafka Cluster              │
     │                                   │
     │      raw-events-topic             │
     │   processed-events-topic          │
     │         alerts-topic              │
     └─────────--──────────────────────--┘
                  │
     ┌────────────▼─────────────┐
     │   Consumer Applications  │
     │  (Stream Processors)     │
     └────────────┬─────────────┘
                  │
     ┌────────────▼─────────────-┐
     │ Real-Time Processing Layer│
     └────────────┬────────────-─┘
                  │
     ┌────────────▼─────────────┐
     │  Sink Layer              │
     │  - PostgreSQL (analytics)│
     │  - Parquet files (batch) │
     └──────────────────────────┘

```
---
## 🔄 Data Flow
1. Event producers generate structured real-time events
2. Events are published to Kafka raw-events-topic
3. Kafka distributes events across partitions for scalability
4. Consumers subscribe via consumer groupss
5. Stream processors transform and analyze events in real time
6. Processed events are published to:
     - processed-events-topic
     - alerts-topic (if anomalies detected)
7. Final data is stored in:
     - PostgreSQL for analytics queries
     - Parquet files for downstream batch processing (Project 6 integration)
   
---
## 📦 Event Schema Design

Each event follows a structured format:

- event_id → unique identifier
- event_type → type of event (trade, click, etc.)
- timestamp → event generation time
- source → origin system
- payload → event-specific data

This ensures consistency across producers and consumers.

---

## 🧰 Tech Stack
- Apache Kafka → Distributed streaming platform
- Python → Producer & consumer implementation
- Docker → local Kafka environment
- PostgreSQL → structured analytics sink
- Parquet files → batch analytics storage
- Pandas (optional) → Lightweight stream processing

---

## ⚙️ Key Streaming Concepts Implemented
### 1. Multi-Topic Architecture

The system uses multiple Kafka topics:

- raw-events-topic → incoming events
- processed-events-topic → cleaned/transformed events
- alerts-topic → anomaly detection outputs

👉 This separates responsibilities and improves scalability.

### 2. Producer-Consumer Decoupling

Kafka acts as a buffer layer, allowing producers and consumers to operate independently without direct dependency.

### 3. Partitioning Strategy
Events are partitioned using keys such as:

- user_id
- event_type

### Why partitioning matters:
- Enables parallel processing
- Maintains ordering per key
- Improves throughput under load

### 3. Consumer Groups

Multiple consumers can process different partitions in parallel, enabling horizontal scaling.

### 4. Real-Time Processing

The system performs real-time transformations such as:

- 1-minute rolling window aggregation of event volume per user
- event filtering and validation
- anomaly detection (e.g., spike in event rate > threshold)
- structured enrichment for downstream systems

---

## 🚨 Failure Handling & Reliability Design

This system includes production-like design considerations:

- Retry mechanisms for failed processing
- Dead Letter Queue (DLQ) via Kafka topic for failed events
- Consumer lag monitoring considerations
- Offset management for resumable processing
- Stateless consumer design for reprocessing capability
- Kafka durability ensures no data loss

---

## 🔗 Connection to Analytics Platform (Project 6)

This project forms the real-time ingestion layer of a larger data platform:

- Project 5 → streaming event ingestion + processing
- Project 6 → batch analytics + data warehouse modeling

Together they simulate a hybrid modern data platform (streaming + batch analytics).

---

## ⚠️ Limitations & Trade-offs 
- Single-node Kafka setup (no full cluster orchestration)
- No schema registry (manual schema enforcement)
- No enterprise-grade monitoring (Prometheus/Grafana not included)
- Simplified stream processing logic for educational clarity

---

## ▶️ How to Run
```bash
# Start Kafka infrastructure
docker-compose up

# Start producer
python producer.py

# Start consumer
python consumer.py
```
---

## 📊 Output Examples
- Real-time event streams processed from Kafka
- Aggregated rolling window metrics
- Anomaly detection alerts (alerts topic)
- Structured datasets stored in PostgreSQL
- Parquet files for batch analytics pipelines

---

## 💡 Key Learnings
- Kafka architecture and distributed messaging
- Real-time stream processing design
- Producer–consumer patterns at scale
- Partitioning and parallel processing concepts
- Event-driven system design
- Hybrid streaming + batch data platform thinking

It bridges the gap between batch ETL systems and real-time event processing systems.


