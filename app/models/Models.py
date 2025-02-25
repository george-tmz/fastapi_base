from sqlalchemy import Column, Integer, String, DateTime

from core.DbConnect import Base


class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    task_id = Column(String(64))
    source_video_url = Column(String(255))
    status = Column(Integer)
    failed_info = Column(String(255))
    host_id = Column(String(20))
    account = Column(String(50))
    model_id = Column(String(64))
    model_path = Column(String(255))
    cover_url = Column(String(255))
    finish_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)