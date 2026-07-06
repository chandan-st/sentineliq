import json

from sqlalchemy.orm import Session

from app.models.analysis_history import AnalysisHistory


def save_analysis(
    db: Session,
    event: str,
    analysis: dict,
):
    print("========== SAVE_ANALYSIS CALLED ==========")
    print("EVENT:", event)
    print("TITLE:", analysis.get("title"))
    history = AnalysisHistory(
        event=event,
        title=analysis.get("title"),
        severity=analysis.get("severity"),
        root_cause=analysis.get("root_cause"),
        summary=analysis.get("summary"),
        recommendations=json.dumps(
            analysis.get("recommendations", [])
        ),
        business_impact=analysis.get(
            "business_impact"
        ),
    )

    db.add(history)
    db.commit()
    db.refresh(history)

    print("HISTORY SAVED WITH ID:", history.id)

    return history


def get_history(db: Session):
    return (
        db.query(AnalysisHistory)
        .order_by(
            AnalysisHistory.created_at.desc()
        )
        .all()
    )