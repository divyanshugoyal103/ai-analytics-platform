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