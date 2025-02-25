from sqlalchemy import Boolean, Column, Integer, String

from core.DbConnect import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
