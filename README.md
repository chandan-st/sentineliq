# SentinelIQ 🛡️

> AI-Powered SaaS Incident Intelligence Platform built with FastAPI, PostgreSQL, React, Docker, and Llama3.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![React](https://img.shields.io/badge/React-19-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Overview

SentinelIQ is an AI-powered Incident Intelligence Platform that automatically detects, classifies, and manages incidents using Large Language Models (LLMs).

The platform analyzes system logs and events, determines severity levels, generates remediation recommendations, and provides operational insights through an analytics dashboard.

---

# 🚀 Features

## 🔐 Authentication
- User Registration
- User Login
- JWT Authentication

## 🚨 Incident Management
- Create Incidents
- View Incidents
- Update Incident Status
- Incident Deduplication
- Incident Tracking Dashboard

## 🤖 AI-Powered Incident Analysis
- Automatic Incident Detection
- Severity Classification
- Risk Score Generation
- Root Cause Summary
- AI-generated Recommendations
- Powered by Llama3 (Ollama)

## 📊 Dashboard Analytics
- Total Incidents
- Open vs Resolved Incidents
- Severity Distribution
- Recent Incidents

---

# 🏗️ System Architecture

```text
                +-------------------+
                |   React Frontend  |
                +-------------------+
                          |
                          |
                          ▼
                +-------------------+
                |   FastAPI Backend |
                +-------------------+
                          |
          --------------------------------
          |                              |
          ▼                              ▼
+-------------------+        +-------------------+
|    PostgreSQL     |        |   Ollama Llama3   |
|     Database      |        |     AI Engine     |
+-------------------+        +-------------------+
```

---

# 🛠️ Tech Stack

## Frontend
- React
- Vite
- Tailwind CSS
- Axios
- React Query
- Recharts
- Framer Motion
- React Hot Toast

## Backend
- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication

## Database
- PostgreSQL

## AI & Machine Learning
- Ollama
- Llama3

## DevOps
- Docker
- GitHub
- Jenkins (Upcoming)
- CI/CD Pipeline (Upcoming)

---

# 📂 Project Structure

```text
sentineliq/
│
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   └── services/
│   │
│   └── requirements.txt
│
├── frontend/
│
├── docker-compose.yml
│
└── README.md
```

---

# ⚡ API Endpoints

## Authentication

```http
POST /api/auth/register
POST /api/auth/login
```

---

## Incidents

```http
GET    /api/incidents
POST   /api/incidents
PUT    /api/incidents/{id}
DELETE /api/incidents/{id}
```

---

## AI Analysis

```http
POST /api/events/analyze
```

Automatically:

- Analyzes logs
- Classifies severity
- Generates recommendations
- Creates incidents in PostgreSQL

---

## Dashboard

```http
GET /api/dashboard/metrics
GET /api/dashboard/recent
GET /api/dashboard/severity
```

---

# 🧠 AI Workflow

```text
Logs / Events
      ↓
Llama3 Analysis
      ↓
Severity Classification
      ↓
Risk Score Generation
      ↓
Recommendations
      ↓
Automatic Incident Creation
      ↓
PostgreSQL Storage
      ↓
Dashboard Analytics
```

---

# 🚀 Running Locally

## 1. Clone Repository

```bash
git clone https://github.com/chandan-st/sentineliq.git
cd sentineliq
```

---

## 2. Start PostgreSQL

```bash
docker compose up -d
```

---

## 3. Start Backend

```bash
cd backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 4. Start Ollama

```bash
ollama serve
```

Pull Llama3:

```bash
ollama pull llama3
```

---

## 5. Start Frontend

```bash
cd frontend

npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 📈 Current Features Implemented

✅ Authentication System

✅ JWT Authorization

✅ Incident CRUD APIs

✅ AI Incident Analysis using Llama3

✅ Automatic Incident Creation

✅ Incident Deduplication

✅ Dashboard Analytics APIs

✅ Dockerized PostgreSQL

✅ GitHub Integration

---

# 📌 Sample AI Incident Analysis

### Input

```text
Database timeout. CPU usage reached 98%. Services unavailable.
```

### Output

```json
{
  "title": "Database Timeout",
  "severity": "High",
  "risk_score": 80,
  "summary": "CPU usage reached 98%, services unavailable due to database timeout.",
  "recommendations": [
    {
      "step": "Increase database instance size"
    },
    {
      "step": "Optimize database queries"
    },
    {
      "step": "Implement connection pooling"
    }
  ]
}
```

---

# 📊 Dashboard Metrics Example

```json
{
  "total_incidents": 3,
  "critical": 2,
  "high": 1,
  "medium": 0,
  "low": 0,
  "open": 3,
  "resolved": 0
}
```

---

# 🔮 Future Enhancements

- Real-Time Incident Monitoring
- WebSocket Notifications
- Executive PDF Reports
- Multi-Tenant Support
- Kubernetes Deployment
- Jenkins CI/CD Pipeline
- Prometheus Integration
- Grafana Dashboards
- Predictive Incident Intelligence

---

# 💼 Resume Highlights

- Built an AI-powered Incident Intelligence Platform using FastAPI, PostgreSQL, Docker, and Llama3.
- Designed an automated incident detection and severity classification engine.
- Implemented AI-generated remediation recommendations.
- Developed analytics dashboard APIs and incident deduplication engine.
- Integrated local LLMs (Llama3 via Ollama) for intelligent incident analysis.
- Designed scalable REST APIs and containerized services using Docker.

---

# 👨‍💻 Author

**Chandan S T**

GitHub: https://github.com/chandan-st

LinkedIn: https://www.linkedin.com/

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

# 📜 License

This project is licensed under the MIT License.
