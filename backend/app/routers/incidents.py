from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.incident import (
    IncidentCreate,
    IncidentUpdate,
    IncidentResponse,
)
from app.services.incident_service import (
    create_incident,
    get_incidents,
    get_incident,
    update_incident,
    delete_incident,
)
from app.services.ai_service import (
    analyze_incident_with_context,
)
from app.services.history_service import (
    save_analysis,
)
from app.models.incident import Incident
from app.schemas.check_incident import (
    IncidentCheckRequest,
)

router = APIRouter(
    prefix="/api/incidents",
    tags=["Incidents"],
)


@router.post(
    "",
    response_model=IncidentResponse,
)
def create(
    incident: IncidentCreate,
    db: Session = Depends(get_db),
):
    if not incident.title or not incident.title.strip():
        incident.title = (
            incident.description[:60]
            if incident.description
            else "Untitled Incident"
        )

    return create_incident(db, incident)


@router.get(
    "",
    response_model=list[IncidentResponse],
)
def get_all(
    db: Session = Depends(get_db),
):
    return get_incidents(db)


@router.get(
    "/{incident_id}",
    response_model=IncidentResponse,
)
def get_one(
    incident_id: int,
    db: Session = Depends(get_db),
):
    incident = get_incident(db, incident_id)

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return incident


@router.put(
    "/{incident_id}",
    response_model=IncidentResponse,
)
def update(
    incident_id: int,
    incident: IncidentUpdate,
    db: Session = Depends(get_db),
):
    db_incident = update_incident(
        db,
        incident_id,
        incident,
    )

    if not db_incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return db_incident


@router.delete("/{incident_id}")
def delete(
    incident_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_incident(
        db,
        incident_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return {"message": "Incident deleted"}


@router.post("/check")
def check_incident(
    request: IncidentCheckRequest,
    db: Session = Depends(get_db),
):
    print("/api/incidents/check endpoint hit")
    ai_result = analyze_incident_with_context(
        request.event
    )

    save_analysis(
        db,
        request.event,
        ai_result,
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
            "risk_score": ai_result.get("risk_score", 50),
            "root_cause": ai_result.get("root_cause"),
            "summary": ai_result.get("summary"),
            "recommendations": ai_result.get("recommendations", []),
            "business_impact": ai_result.get("business_impact"),
            "message": "Existing incident found."
        }

    incident = Incident(
        title=ai_result["title"],
        description=ai_result.get("summary", request.event),
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
        "risk_score": ai_result.get("risk_score", 50),
        "root_cause": ai_result.get("root_cause"),
        "summary": ai_result.get("summary"),
        "recommendations": ai_result.get("recommendations", []),
        "business_impact": ai_result.get("business_impact"),
    }