from sqlalchemy import Column, Integer, String, DateTime
from backend.core.database import Base

class UserAuth(Base):
    __tablename__ = "userauth"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    updatedat = Column(DateTime)
    deletedat = Column(DateTime, nullable=True)
