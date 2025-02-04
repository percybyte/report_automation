# app/models/order.model.py

from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    total_amount = Column(Float)
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(
        String, default="pending"
    )  # Status order (pending, complete, cancelled)

    client = relationship("Client", back_populates="orders")
