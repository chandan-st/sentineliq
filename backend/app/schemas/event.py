from pydantic import BaseModel


class EventRequest(BaseModel):
    message: str