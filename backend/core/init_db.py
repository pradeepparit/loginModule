# app/core/init_db.py
from app.core.database import engine
from app.models import User, UserAuth, Investment, Expenses, Savings, Category

def init_db():
    # Create all tables (if they don't already exist)
    from app.core.database import Base
    Base.metadata.create_all(bind=engine)
