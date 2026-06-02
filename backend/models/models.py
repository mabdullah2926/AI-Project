from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from backend.database.db import Base

class Return(Base):
    __tablename__ = "returns"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, index=True)
    customer_name = Column(String)
    product_name = Column(String)
    reason = Column(String)
    condition = Column(String)
    status = Column(String, default="pending")
    refund_amount = Column(Float, default=0.0)
    agent_decision = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())