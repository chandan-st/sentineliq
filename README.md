# 🛡️ SentinelIQ
### AI-Powered Incident Intelligence Platform using Llama3 and RAG

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/React-Frontend-blue?style=for-the-badge&logo=react" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql" />
  <img src="https://img.shields.io/badge/AI-Llama3-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RAG-FAISS-purple?style=for-the-badge" />
</p>

---

# 📌 Overview

**SentinelIQ** is an AI-powered Incident Intelligence Platform designed to assist organizations in detecting, analyzing, and managing operational incidents using **Large Language Models (LLMs)** and **Retrieval-Augmented Generation (RAG)**.

The platform analyzes incident logs, identifies root causes, estimates business impact, generates contextual recommendations, and maintains a complete incident history for future reference.

---

# 🚀 Features

### 🤖 AI Incident Analysis
- Incident classification using **Llama3**
- Root cause identification
- Risk score generation
- Business impact analysis
- Intelligent recommendations

### 🧠 Retrieval-Augmented Generation (RAG)
- Semantic similarity search using **Sentence Transformers**
- Incident knowledge base retrieval
- Context-aware recommendations
- Historical incident matching

### 📊 Dashboard
- Total incidents
- Open incidents
- Critical incidents
- Incident severity distribution
- Recent incidents overview

### 📂 Incident Management
- Create incidents automatically
- View incident details
- Delete incidents
- Track incident status

### 🕒 Analysis History
- Stores:
  - Event
  - AI Summary
  - Root Cause
  - Recommendations
  - Business Impact
  - Risk Score
  - Timestamp

### 📑 Reports
- Export reports as CSV
- Incident analytics
- Historical tracking

### 🔐 Authentication
- User Registration
- Login System
- JWT Authentication

---

# 🏗️ System Architecture

```text
┌──────────────────┐
│     Frontend     │
│      React       │
└────────┬─────────┘
         │ REST API
         ▼
┌──────────────────┐
│     FastAPI      │
│      Backend     │
└────────┬─────────┘
         │
         ├────────► PostgreSQL
         │
         ├────────► FAISS Vector DB
         │
         └────────► Ollama + Llama3
```

---

# 🛠️ Tech Stack

## Frontend
- React.js
- Vite
- Tailwind CSS
- Axios
- React Query
- React Router
- Lucide Icons

## Backend
- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication
- Alembic

## Database
- PostgreSQL

## AI & Machine Learning
- Ollama
- Llama3
- Sentence Transformers
- FAISS
- RAG Pipeline

## Tools & DevOps
- Git
- GitHub
- Docker
- Render
- Vercel

---

# 📁 Project Structure

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
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── incident_index.faiss
│   ├── incident_metadata.pkl
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── layouts/
│   │   └── App.jsx
│   │
│   └── package.json
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/chandan-st/sentineliq.git
cd sentineliq
```

---

# Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
# Windows:
# venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# Environment Variables

## Backend `.env`

```env
DATABASE_URL=postgresql://username:password@localhost/sentineliq
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
OLLAMA_URL=http://127.0.0.1:11434/api/generate
```

---

# Frontend `.env`

```env
VITE_API_URL=http://127.0.0.1:8000
```

---

# Running Ollama

Install Ollama:

```bash
brew install ollama
```

Pull Llama3:

```bash
ollama pull llama3
```

Start Ollama:

```bash
ollama serve
```

---

# AI Workflow

```text
Incident Event
      │
      ▼
Llama3 Analysis
      │
      ▼
RAG Context Retrieval
      │
      ▼
Root Cause Analysis
      │
      ▼
Recommendations
      │
      ▼
Business Impact Assessment
      │
      ▼
Store in History
```

---

# API Endpoints

## Authentication

| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | /register | Register User |
| POST | /login | Login User |

---

## Incidents

| Method | Endpoint |
|--------|-----------|
| POST | /api/incidents/check |
| GET | /api/incidents |
| DELETE | /api/incidents/{id} |

---

## History

| Method | Endpoint |
|--------|-----------|
| GET | /api/history |

---

## Dashboard

| Method | Endpoint |
|--------|-----------|
| GET | /api/dashboard |

---

# Screenshots

Add screenshots here:

```text
Dashboard Screenshot
Incident Analysis Screenshot
History Screenshot
Reports Screenshot
```

---

# Future Enhancements

- Email Alerts
- Real-Time Monitoring
- Kafka Integration
- Kubernetes Deployment
- Multi-Tenant Architecture
- Redis Caching
- Incident Prediction
- AI Chat Assistant
- Role-Based Access Control

---

# Deployment Note

The application is fully functional in a local environment.

Due to memory limitations of free cloud instances, AI inference using **Llama3**, **Sentence Transformers**, and **FAISS** is demonstrated locally. The platform can be deployed to production environments with higher-memory compute instances.

---

# Author

## Chandan S T

- GitHub: https://github.com/chandan-st
- LinkedIn:https://www.linkedin.com/in/chandan-s-t-0585222a1/

---

# License

This project is developed for educational and research purposes.

---

# ⭐ If you found this project useful, consider giving it a star.
