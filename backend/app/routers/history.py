from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json

from app.db.dependencies import get_db
from app.services.history_service import get_history

router = APIRouter(
    prefix="/api/history",
    tags=["History"],
)


@router.get("")
def history(
    db: Session = Depends(get_db),
):
    history_items = get_history(db)

    for item in history_items:
        try:
            item.recommendations = json.loads(
                item.recommendations
            ) if item.recommendations else []
        except Exception:
            item.recommendations = []

    return history_items