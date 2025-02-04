from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import AsyncSessionLocal, engine
from app.models.user_model import User
from app.models.product_model import Product
from app.models.client_model import Client
from app.models.order_model import Order
from app.models.sale_model import Sale
from datetime import datetime, timedelta
import random

fake = Faker()


async def seed_database():
    async with AsyncSessionLocal() as session:
        try:
            # Create users
            users = [
                User(
                    username=fake.user_name(),
                    email=fake.email(),
                    hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # dummy bcrypt hash
                    is_active=True,
                )
                for _ in range(10)
            ]
            session.add_all(users)
            await session.commit()
            # await session.refresh_all(users)
            # for user in users:
            #     await session.refresh(user)

            # Create products
            products = [
                Product(
                    name=fake.catch_phrase(),
                    description=fake.text(max_nb_chars=200),
                    price=round(random.uniform(10, 500), 2),
                    stock=random.randint(10, 500),
                    is_active=True,
                    owner_id=random.choice(users).id,
                )
                for _ in range(50)
            ]
            session.add_all(products)
            await session.commit()
            # for product in products:
            #     await session.refresh(products)

            # Create customers
            clients = [
                Client(
                    name=fake.name(),
                    email=fake.email(),
                    phone=fake.phone_number(),
                    address=fake.address(),
                    total_spent=0.0,
                )
                for _ in range(100)
            ]
            session.add_all(clients)
            await session.commit()
            # for client in clients:
            #     await session.refresh(clients)

            # Create orders
            orders = []
            for _ in range(300):
                client = random.choice(clients)
                total_amount = round(random.uniform(50, 1000), 2)
                order = Order(
                    client_id=client.id,
                    total_amount=total_amount,
                    order_date=fake.date_time_between(start_date="-2y", end_date="now"),
                    status=random.choice(["pending", "complete", "cancelled"]),
                )
                orders.append(order)
                client.total_spent += total_amount

            session.add_all(orders)
            await session.commit()

            # Create sales
            sales = []
            for _ in range(500):
                product = random.choice(products)
                user = random.choice(users)
                quantity = random.randint(1, 10)
                total_price = round(product.price * quantity, 2)

                sale = Sale(
                    product_id=product.id,
                    user_id=user.id,
                    quantity=quantity,
                    total_price=total_price,
                    sale_date=fake.date_time_between(start_date="-2y", end_date="now"),
                )
                sales.append(sale)

                # Update stock
                product.stock -= quantity

            session.add_all(sales)
            await session.commit()

            print("Database seeded successfully!")

        except Exception as e:
            await session.rollback()
            print(f"Error seeding database: {e}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(seed_database())
