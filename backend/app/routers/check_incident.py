from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.check_incident import IncidentCheckRequest
from app.services.ai_service import (
    analyze_incident_with_context
)
from app.services.incident_service import (
    create_incident
)
from app.schemas.incident import (
    IncidentCreate
)

router = APIRouter(
    prefix="/api/incidents",
    tags=["Incident Check"]
)


@router.post("/check")
def check_incident(
    request: IncidentCheckRequest,
    db: Session = Depends(get_db)
):
    ai_result = analyze_incident_with_context(
        request.event
    )

    incident = IncidentCreate(
        title=ai_result["title"],
        description=ai_result.get("summary", request.event),
        severity=ai_result["severity"],
        status="Open",
    )

    created = create_incident(
        db,
        incident
    )

    ai_result["incident_id"] = created.id
    ai_result["incident_created"] = True

    return ai_result