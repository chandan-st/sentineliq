from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.event import EventRequest
from app.services.ai_service import analyze_incident
from app.models.incident import Incident

router = APIRouter(
    prefix="/api/events",
    tags=["AI Analysis"],
)


@router.post("/analyze")
def analyze(
    event: EventRequest,
    db: Session = Depends(get_db),
):
    ai_result = analyze_incident(
        event.message
    )

    existing_incident = (
        db.query(Incident)
        .filter(
            Incident.title == ai_result["title"],
            Incident.status == "Open",
        )
        .first()
    )

    if existing_incident:
        return {
            "incident_id": existing_incident.id,
            "title": existing_incident.title,
            "severity": existing_incident.severity,
            "risk_score": ai_result["risk_score"],
            "summary": ai_result["summary"],
            "recommendations": ai_result["recommendations"],
            "message": "Existing incident found."
        }

    incident = Incident(
        title=ai_result["title"],
        description=ai_result["summary"],
        severity=ai_result["severity"],
        source="AI Analysis",
        status="Open",
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return {
        "incident_id": incident.id,
        "title": incident.title,
        "severity": incident.severity,
        "risk_score": ai_result["risk_score"],
        "summary": ai_result["summary"],
        "recommendations": ai_result["recommendations"],
    }