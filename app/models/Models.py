from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from core.DbConnect import Base


class Model(Base):
    __tablename__ = "models"
    id = Column(Integer, primary_key=True)
    task_id = Column(String(64), default="")
    source_video_url = Column(String(255), default="")
    callback_url = Column(String(255), default="")
    status = Column(Integer, default=0)
    failed_info = Column(String(255), default="")
    host_ip = Column(String(20), default="")
    account = Column(String(50), default="")
    model_id = Column(String(64), default="")
    model_path = Column(String(255), default="")
    cover_url = Column(String(255), default="")
    finish_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
