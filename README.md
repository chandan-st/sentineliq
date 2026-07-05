# SentinelIQ 🛡️

AI-Powered SaaS Incident Intelligence Platform built with FastAPI, PostgreSQL, React, Docker, and Llama3.

## Overview

SentinelIQ automatically detects, classifies, and manages incidents using Artificial Intelligence. The platform analyzes logs and events, determines severity levels, generates remediation recommendations, and provides real-time operational insights through an executive dashboard.

---

## Features

### Authentication
- User Registration
- User Login
- JWT Authentication

### Incident Management
- Create Incidents
- View Incidents
- Update Incident Status
- Incident Deduplication
- Incident Tracking Dashboard

### AI-Powered Incident Analysis
- Automatic Incident Detection
- Severity Classification
- Risk Score Generation
- Root Cause Summary
- AI-generated Recommendations
- Powered by Llama3 (Ollama)

### Dashboard Analytics
- Total Incidents
- Open vs Resolved Incidents
- Severity Distribution
- Recent Incidents

---

## Architecture

```text
React Frontend
       ↓
FastAPI Backend
       ↓
PostgreSQL Database
       ↓
Llama3 (Ollama)
```
