from app.db.database import AsyncSessionLocal
from app.db.repositories.base import BaseRepository
from app.models.order_model import Order
from sqlalchemy import select, func


class OrderRepository(BaseRepository):
    async def get_order_status_summary(self):
        async with AsyncSessionLocal() as session:
            query = select(Order.status, func.count(Order.id)).group_by(Order.status)

            result = await session.execute(query)
            return dict(result.all())
