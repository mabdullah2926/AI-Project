from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.agents.analytics_agent import run as analytics_run
from backend.database.db import get_db
from backend.models.models import Return


router = APIRouter(prefix="/api/analytics", tags=["analytics"])


def _serialize_return(record: Return) -> dict:
    return {
        "id": record.id,
        "order_id": record.order_id,
        "customer_name": record.customer_name,
        "product_name": record.product_name,
        "reason": record.reason,
        "condition": record.condition,
        "status": record.status,
        "refund_amount": record.refund_amount,
        "agent_decision": record.agent_decision,
        "created_at": record.created_at.isoformat() if record.created_at else None,
    }


@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    records = [_serialize_return(record) for record in db.query(Return).all()]
    return analytics_run({"all_records": records})["analytics"]

