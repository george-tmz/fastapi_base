from sqlalchemy import Column, Integer, String, DateTime

from core.DbConnect import Base


class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    task_id = Column(String(64))
    source_audio_url = Column(String(255))
    audio_path = Column(String(255))
    model_id = Column(String(64))
    status = Column(Integer)
    failed_info = Column(String(255))
    host_id = Column(String(20))
    account = Column(String(50))
    finish_at = Column(DateTime)
    video_url = Column(String(255))
    video_url_oss = Column(String(255))
    cover_url = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)