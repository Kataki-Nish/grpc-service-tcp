# Resilient gRPC Service Framework (TCP Transport)

A production-grade Python gRPC chassis demonstrating system engineering best practices, graceful shutdown handling, custom client authority resolution, and Dockerized deployment.

## 🌟 Key Architectural Features

- **Graceful Shutdown**: Handles `SIGTERM` and `SIGINT` signals safely via Python `Lifespan` concepts, avoiding connection drops or data corruption during container lifecycle events.
- **Base Server & Client Abstractions**: Encapsulates core gRPC setup, channel management, and lifecycle events into clean base classes.
- **Custom Authority Resolver**: Supports full control over connection targets for TCP (and expandable to UDS local IPC).
- **Containerized Pipeline**: Fully configured with `Dockerfile` and `docker-compose.yml` for multi-container orchestration.

## 📁 Project Structure
```text
├── base_class.py         # Abstract base server with signal handling
├── client.py             # Resilient gRPC client with custom authority resolution
├── server.py             # Service implementation
├── test.proto            # Protocol Buffer schema
├── test_pb2*.py          # Generated gRPC stubs
├── docker-compose.yml    # Orchestration configuration
└── Dockerfile            # Container build instructions

## 🔥Getting Started

### Prerequisites
- Python 3.10+
- Docker & Docker Compose

### Running via Docker
bash
docker-compose up --build

