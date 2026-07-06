from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
)

from sqlalchemy.sql import func

from app.db.database import Base


class AnalysisHistory(Base):
    __tablename__ = "analysis_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    event = Column(Text)

    title = Column(String)

    severity = Column(String)

    root_cause = Column(Text)

    summary = Column(Text)

    recommendations = Column(Text)

    business_impact = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )