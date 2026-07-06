from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.models import User, Incident

from app.routers.auth import router as auth_router
from app.routers.incidents import router as incident_router
from app.routers.events import router as event_router
from app.routers.dashboard import router as dashboard_router
from app.routers.history import (
    router as history_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SentinelIQ API",
    version="1.0.0"
)

# CORS Configuration
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router)
app.include_router(incident_router)
app.include_router(event_router)
app.include_router(dashboard_router)
app.include_router(history_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to SentinelIQ 🚀"
    }