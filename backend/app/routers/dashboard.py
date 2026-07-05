from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.incident import Incident

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"],
)


@router.get("/metrics")
def get_metrics(
    db: Session = Depends(get_db),
):
    total_incidents = db.query(Incident).count()

    critical = (
        db.query(Incident)
        .filter(Incident.severity == "Critical")
        .count()
    )

    high = (
        db.query(Incident)
        .filter(Incident.severity == "High")
        .count()
    )

    medium = (
        db.query(Incident)
        .filter(Incident.severity == "Medium")
        .count()
    )

    low = (
        db.query(Incident)
        .filter(Incident.severity == "Low")
        .count()
    )

    open_incidents = (
        db.query(Incident)
        .filter(Incident.status == "Open")
        .count()
    )

    resolved_incidents = (
        db.query(Incident)
        .filter(Incident.status == "Resolved")
        .count()
    )

    return {
        "total_incidents": total_incidents,
        "critical": critical,
        "high": high,
        "medium": medium,
        "low": low,
        "open": open_incidents,
        "resolved": resolved_incidents,
    }
@router.get("/recent")
def get_recent_incidents(
    db: Session = Depends(get_db),
):
    incidents = (
        db.query(Incident)
        .order_by(Incident.created_at.desc())
        .limit(10)
        .all()
    )

    return incidents

@router.get("/severity")
def get_severity_distribution(
    db: Session = Depends(get_db),
):
    return {
        "Critical": (
            db.query(Incident)
            .filter(Incident.severity == "Critical")
            .count()
        ),
        "High": (
            db.query(Incident)
            .filter(Incident.severity == "High")
            .count()
        ),
        "Medium": (
            db.query(Incident)
            .filter(Incident.severity == "Medium")
            .count()
        ),
        "Low": (
            db.query(Incident)
            .filter(Incident.severity == "Low")
            .count()
        ),
    }