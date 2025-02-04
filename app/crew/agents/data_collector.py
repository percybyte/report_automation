from crewai import Agent
from langchain_openai import ChatOpenAI
from app.db.repositories.product_repository import ProductRepository
from app.db.repositories.sale_repository import SaleRepository
from app.db.repositories.order_repository import OrderRepository
from typing import List, Dict, Any
import os


class DataCollectorAgent(Agent):
    def __init__(
        self,
        product_repository: ProductRepository,
        sale_repository: SaleRepository,
        order_repository: OrderRepository,
        llm: ChatOpenAI = None,
    ):
        super().__init__(
            role="Data Collection Specialist",
            goal="Retrieve comprehensive and accurate data for business reports",
            backstory="""
            You are a meticulous data collection expert who can extract
            precise information from various repositories. Your ability
            to gather and organize data is crucial for generating
            insightful business reports.
            """,
            verbose=True,
            llm=llm or ChatOpenAI(temperature=0.2),
        )
        self.product_repository = product_repository
        self.sale_repository = sale_repository
        self.order_repository = order_repository

    async def collect_sales_report_data(self, days: int = 30) -> Dict[str, Any]:
        """
        Collect sales data for report generation

        Args:
            days (int): Number of days to collect data for

        Returns:
            Dict containing sales metrics
        """
        sales_summary = await self.sale_repository.get_total_sales()
        top_products = await self.product_repository.get_top_selling_products()

        return {
            "sales_summary": sales_summary,
            "top_products": [
                {
                    "id": product.id,
                    "name": product.name,
                    "total_sales": product.total_sales,
                }
                for product in top_products
            ],
        }

    async def collect_inventory_report_data(
        self, low_stock_threshold: int = 20
    ) -> Dict[str, Any]:
        """
        Collect inventory data for report generation

        Args:
            low_stock_threshold (int): Threshold for low stock products

        Returns:
            Dict containing inventory metrics
        """
        low_stock_products = await self.product_repository.get_low_stock_products(
            threshold=low_stock_threshold
        )

        return {
            "low_stock_products": [
                {"id": product.id, "name": product.name, "current_stock": product.stock}
                for product in low_stock_products
            ]
        }

    async def collect_distribution_report_data(self) -> Dict[str, Any]:
        """
        Collect order distribution data for report generation

        Returns:
            Dict containing order distribution metrics
        """
        order_status_summary = await self.order_repository.get_order_status_summary()

        return {"order_status_summary": order_status_summary}
