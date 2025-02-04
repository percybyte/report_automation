# app/models/sale.model.py
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(
        Integer, ForeignKey("products.id"), nullable=False
    )  # Relation with products
    user_id = Column(
        Integer, ForeignKey("users.id"), nullable=False
    )  # Relation with users
    quantity = Column(Integer, nullable=False)  # Sales quantity
    total_price = Column(Float, nullable=False)
    sale_date = Column(DateTime, default=func.now())

    # Relations with products and users
    product = relationship("Product", backref="sales")
    user = relationship("User", backref="sales")
