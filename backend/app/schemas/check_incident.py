from pydantic import BaseModel


class IncidentCheckRequest(BaseModel):
    event: str

class IncidentCheckResponse(BaseModel):
    title: str
    severity: str
    risk_score: int
    summary: str
    recommendations: list[str]
    incident_created: bool