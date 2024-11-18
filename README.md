
# Kafka with KRaft Mode and Apache Druid Integration

This project demonstrates how to set up a Kafka cluster using KRaft mode (without Zookeeper) and integrate it with Apache Druid for data analytics and visualization.

## Project Overview

- **Kafka in KRaft mode**: A modern setup for Kafka that replaces Zookeeper with a self-managed metadata quorum.
- **Apache Druid**: A high-performance, real-time analytics database integrated with Kafka for efficient querying and visualization.

### Key Features

- Fully containerized Kafka cluster in KRaft mode (no Zookeeper).
- Apache Druid cluster for real-time ingestion and querying.
- Integration with PostgreSQL for Druid metadata storage.

## Architecture

1. **Kafka (KRaft Mode)**:
   - A 3-node Kafka cluster (1 controller, 2 brokers).
   - KRaft replaces Zookeeper for metadata management.
   - Designed for high availability and scalability.
   - ![Kraft-Kafka](/kraft-kafka_arch.png)

2. **Apache Druid**:
   - Includes Coordinator, Broker, Historical, MiddleManager, and Router nodes.
   - Ingests data from Kafka topics for real-time analytics.
   - Stores metadata in a PostgreSQL database.
   - ![Apache-Druid](/druid_arch.png)


## Prerequisites

- Docker and Docker Compose installed on your machine.
- Minimum hardware requirements:
  - 4 GB RAM
  - Quad-core processor

## Setup Instructions

### 1. Clone the Repository

```bash
git clone [https://github.com/evanmathew/Apache-Kafka-Kraft-and-Apache-Druid.git](https://github.com/evanmathew/Apache-Kafka-Kraft-and-Apache-Druid.git
cd Apache-Kafka-Kraft-and-Apache-Druid
```

### 2. Update Environment Variables

Ensure the following variables are set in the `environment` file:
- **PostgreSQL Database**:
  - `POSTGRES_PASSWORD`: Set the password for the `druid` user.
  - `POSTGRES_USER`: The database username (default: `druid`).
  - `POSTGRES_DB`: The database name (default: `druid`).

### 3. Start the Services

```bash
docker-compose up -d
```

### 4. Access the Services

- **Druid Router**: `http://localhost:8888`
- **Kafka Brokers**: Exposed on ports `29092`, `39092`.

### 5. Run main.py Python File 

- **Install virtual env.**: python -m venv venv
- **Initiate venv**: venv/Scripts/activate
- **Run the code which will produce the random sample data and stream to kafka using producer**


### 6. Configure Druid Ingestion

1. Access the Druid Router UI (`http://localhost:8888`).
2. Navigate to `Load Data` and select `Apache Kafka`.
3. Configure the Kafka topic to ingest data.
   - **bootstrap server**: `broker-1:19092,broker-2:19092`
   - **topic name**: `ecommerce_event_data`
   - **Start parsing the data**
     
## Configuration Details

### Kafka KRaft Configuration

- **controller.quorum.voters**: Defines the controller quorum.
- **process.roles**: Specifies whether a node is a `broker`, `controller`, or `broker,controller`
- **node.id**: Unique identifier for each node in the cluster.

### Druid Configuration

- Druid relies on Kafka for real-time data ingestion.
- Metadata is stored in PostgreSQL, mounted as a volume.

## Troubleshooting

1. **Kafka is not starting**: Ensure the `controller.quorum.voters` setting is correct in the `docker-compose.yml`.
2. **Druid UI not accessible**: Verify that the ports are not blocked or in use by other applications.

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request.



---

Happy Streaming and Querying! 🚀
