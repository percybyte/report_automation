from crewai import Task
from typing import Dict, Any


class ExtractionTask:
    @staticmethod
    def sales_data_extraction_task(agent, report_type: str = "sales"):
        """
        Create a task for extracting sales-related data

        Args:
            agent: DataCollectorAgent instance
            report_type: Type of report to extract (sales, inventory, distribution)

        Returns:
            CrewAI Task for data extraction
        """
        return Task(
            description=f"""
            Extract comprehensive data for {report_type.capitalize()} Report.

            Guidelines:
            - Retrieve all relevant data from repositories
            - Ensure data accuracy and completeness
            - Organize data in a structured format
            - Prepare data for further analysis

            Report Type: {report_type}
            """,
            agent=agent,
            async_execution=True,
            expected_output=f"""
            A detailed dictionary containing {report_type} metrics with the following characteristics:
            - Structured data format
            - Comprehensive coverage of key metrics
            - Ready for analysis by the next agent in the workflow
            """,
        )

    @staticmethod
    def inventory_data_extraction_task(agent, report_type: str = "inventory"):
        """
        Create a task for extracting inventory-related data

        Args:
            agent: DataCollectorAgent instance
            report_type: Type of report to extract

        Returns:
            CrewAI Task for data extraction
        """
        return Task(
            description=f"""
            Extract comprehensive data for {report_type.capitalize()} Report.

            Guidelines:
            - Identify products with low stock
            - Collect current inventory status
            - Ensure data accuracy and completeness
            - Organize data in a structured format

            Report Type: {report_type}
            """,
            agent=agent,
            async_execution=True,
            expected_output=f"""
            A detailed dictionary containing {report_type} metrics with the following characteristics:
            - List of low stock products
            - Current inventory status
            - Structured data format
            - Ready for analysis by the next agent in the workflow
            """,
        )

    @staticmethod
    def distribution_data_extraction_task(agent, report_type: str = "distribution"):
        """
        Create a task for extracting distribution-related data

        Args:
            agent: DataCollectorAgent instance
            report_type: Type of report to extract

        Returns:
            CrewAI Task for data extraction
        """
        return Task(
            description=f"""
            Extract comprehensive data for {report_type.capitalize()} Report.
            
            Guidelines:
            - Collect order status summary
            - Analyze distribution metrics
            - Ensure data accuracy and completeness
            - Organize data in a structured format
            
            Report Type: {report_type}
            """,
            agent=agent,
            async_execution=True,
            expected_output=f"""
            A detailed dictionary containing {report_type} metrics with the following characteristics:
            - Order status breakdown
            - Distribution performance indicators
            - Structured data format
            - Ready for analysis by the next agent in the workflow
            """,
        )
