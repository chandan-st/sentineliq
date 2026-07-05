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
    return create_incident(
        db,
        incident,
    )


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
    incident = get_incident(
        db,
        incident_id,
    )

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


@router.delete(
    "/{incident_id}",
)
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

    return {
        "message": "Incident deleted"
    }