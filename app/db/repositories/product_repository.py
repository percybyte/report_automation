from app.db.database import AsyncSessionLocal
from app.db.repositories.base import BaseRepository
from app.models.product_model import Product
from sqlalchemy import select


class ProductRepository(BaseRepository):
    async def get_low_stock_products(self, threshold=20):
        async with AsyncSessionLocal() as session:
            query = select(Product).filter(Product.stock <= threshold)
            result = await session.execute(query)
            return result.scalars().all()

    async def get_top_selling_products(self, limit=5):
        async with AsyncSessionLocal() as session:
            # Esta consulta dependerá de cómo esté estructurada tu relación entre Product y Sale
            query = select(Product).order_by(Product.total_sales.desc()).limit(limit)
            result = await session.execute(query)
            return result.scalars().all()
