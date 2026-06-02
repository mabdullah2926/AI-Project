from __future__ import annotations

from pydantic import BaseModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.agents import (
    analytics_agent,
    classification_agent,
    communication_agent,
    fraud_agent,
    routing_agent,
)
from backend.database.db import get_db
from backend.models.models import Return


router = APIRouter()


class ReturnRequest(BaseModel):
    order_id: str
    customer_name: str
    product_name: str
    reason: str
    condition: str


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


@router.post("/submit")
def submit_return(req: ReturnRequest, db: Session = Depends(get_db)):
    data = req.model_dump()

    data = classification_agent.run(data)
    data = fraud_agent.run(data)
    data = routing_agent.run(data)

    if data["fraud_flag"]:
        data["status"] = "rejected"
        data["refund_amount"] = 0.0
        data["agent_decision"] = f"Rejected: {data['fraud_reason']}"
    elif data["priority"] == "high":
        data["status"] = "approved"
        data["refund_amount"] = 100.0
        data["agent_decision"] = f"Auto-approved: {data['category']} - routed to {data['assigned_team']}"
    else:
        data["status"] = "manual_review"
        data["refund_amount"] = 0.0
        data["agent_decision"] = f"Manual review: {data['category']} - routed to {data['assigned_team']}"

    data = communication_agent.run(data)

    record = Return(
        order_id=data["order_id"],
        customer_name=data["customer_name"],
        product_name=data["product_name"],
        reason=data["reason"],
        condition=data["condition"],
        status=data["status"],
        refund_amount=data["refund_amount"],
        agent_decision=data["agent_decision"],
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    payload = _serialize_return(record)
    payload["customer_message"] = data["customer_message"]
    return payload


@router.get("/all")
def get_all_returns(db: Session = Depends(get_db)):
    records = db.query(Return).order_by(Return.created_at.desc()).all()
    return [_serialize_return(record) for record in records]


@router.get("/analytics")
def get_analytics(db: Session = Depends(get_db)):
    records = [_serialize_return(record) for record in db.query(Return).all()]
    data = {"all_records": records}
    data = analytics_agent.run(data)
    return data["analytics"]

