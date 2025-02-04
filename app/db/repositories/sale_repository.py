from app.db.database import AsyncSessionLocal
from app.db.repositories.base import BaseRepository
from app.models.sale_model import Sale
from sqlalchemy import select, func
from datetime import datetime, timedelta


class SaleRepository(BaseRepository):
    async def get_total_sales(self, start_date=None, end_date=None):
        async with AsyncSessionLocal() as session:
            if not start_date:
                start_date = datetime.now() - timedelta(days=30)
            if not end_date:
                end_date = datetime.now()

            query = select(func.sum(Sale.total_amount), func.count(Sale.id)).filter(
                Sale.sale_date.between(start_date, end_date)
            )
            result = await session.execute(query)
            total_amount, total_sales = result.first()
            return {"total_amount": total_amount or 0, "total_sales": total_sales or 0}
