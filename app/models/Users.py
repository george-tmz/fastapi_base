from core.DbConnect import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
