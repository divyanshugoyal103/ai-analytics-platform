# AI Analytics Platform

A **high-performance, privacy-first AI data analytics platform** that allows users to upload datasets, ask questions in natural language, and generate instant insights, charts, and dashboards.

The system behaves like a **professional AI data analyst**, combining **DuckDB, Polars, and AI agents** to deliver extremely fast analytics while keeping data local and secure.

---

# Overview

AI Analytics Platform enables users to:

- Upload datasets (CSV, Excel, Parquet)
- Ask analytics questions in natural language
- Automatically generate SQL queries
- Run analytics instantly
- Create visualizations and dashboards
- Generate AI insights and reports
- Explore datasets automatically

The platform prioritizes:

- Maximum performance
- Local-first architecture
- Data privacy
- Modular AI agent system
- Scalable analytics engine

---

# Key Features

## Dataset Upload

Upload datasets in multiple formats:

- CSV
- Excel
- Parquet

Datasets are automatically:

- Converted to **Parquet**
- Registered as **DuckDB tables**
- Profiled for AI metadata

---

## Natural Language Analytics

Ask questions like:

"Which region has the highest revenue growth?"

The system automatically:

1. Understands dataset schema  
2. Generates SQL queries  
3. Validates SQL queries  
4. Executes analytics queries  
5. Generates charts  
6. Provides AI-generated insights  

---

# AI Agent System

The platform uses specialized AI agents:

### Planner Agent
Breaks down the user request into analytical steps.

### SQL Generator Agent
Generates optimized SQL queries from natural language.

### Query Validator Agent
Ensures queries are safe, valid, and efficient.

### Data Analysis Agent
Executes analytics using **DuckDB** and **Polars**.

### Visualization Agent
Automatically selects and generates charts.

### Insight Agent
Converts data results into human-readable insights.

### Report Agent
Generates full analytical reports.

---

# Architecture

```
User Interface
      ↓
Next.js Frontend
      ↓
FastAPI Backend
      ↓
AI Orchestrator
      ↓
Agent System
      ↓
DuckDB + Polars Analytics Engine
      ↓
Parquet Dataset Storage
```

---

# Technology Stack

## Frontend
- Next.js
- Tailwind CSS
- Apache ECharts

## Backend
- Python
- FastAPI

## Analytics Engine
- DuckDB
- Polars

## AI System
- LangChain
- Ollama (local AI models)

## Storage
- Parquet files

## Infrastructure
- Docker
- Kubernetes

---

# Performance

Designed for high-performance analytics:

- Most queries execute **under 1 second**
- Supports **100M+ row datasets**
- DuckDB **vectorized execution**
- Polars **parallel processing**
- Parquet **columnar storage**

---

# Project Structure

```
ai-analytics-platform/

frontend/
  components/
  pages/

backend/
  api/
  agents/
  ai/
  database/
  services/
  models/

datasets/
models/
scripts/

docker/
k8s/

README.md
```

---

# Installation

Clone the repository:

```
git clone https://github.com/your-username/ai-analytics-platform.git
cd ai-analytics-platform
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the backend server:

```
uvicorn backend.main:app --reload
```

API documentation will be available at:

```
http://localhost:8000/docs
```

---

# Example Query

User input:

```
What is the total revenue by region?
```

Generated SQL:

```
SELECT region, SUM(revenue)
FROM sales
GROUP BY region;
```

Generated insight:

Revenue is highest in North America, contributing the largest share of total sales.

---

# Dataset Exploration

Users can run commands such as:

```
Explore this dataset and provide insights.
```

The AI will automatically:

- Analyze dataset structure
- Detect correlations
- Detect anomalies
- Generate charts
- Produce a detailed report

---

# Security & Privacy

Security is a core principle of the platform.

- Datasets **never leave the system**
- AI receives **schema metadata only**
- Queries run in **sandbox environment**
- Optional **local AI models using Ollama**

---

# Deployment

The platform supports deployment via:

- Docker
- Kubernetes
- Local machine
- Cloud infrastructure

Run using Docker:

```
docker-compose up
```

---

# Future Improvements

Planned features include:

- Real-time streaming analytics
- AI dashboard builder
- Anomaly detection agents
- Vector semantic search
- Collaborative dashboards
- Enterprise authentication

---

# Contributing

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

# License

MIT License

---

# Author

Developed by **Divyanshu Goyal**

AI Analytics Platform aims to provide a **next-generation AI-powered analytics system** that is fast, private, and scalable.