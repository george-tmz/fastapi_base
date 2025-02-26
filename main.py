import socket
import uuid

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.models.Models import Model
from app.schemas.ModelCreate import ModelCreate
from config.app import settings
from core.DbConnect import SessionLocal, engine, Base

# create table
Base.metadata.create_all(bind=engine)
app = FastAPI()


# Get db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return "Welcome to here!"


@app.post("/model", response_model=None)
def create_model(data: ModelCreate, db: Session = Depends(get_db)):
    model = Model(
        task_id=get_uuid(),
        source_video_url=data.video_url,
        callback_url=data.callback_url,
        status=1,
        host_ip=get_current_ip()
    )
    db.add(model)
    db.commit()
    db.refresh(model)
    return {
        "code": 200,
        "message": "success",
        "task_id": model.task_id,
        "status": model.status
    }


def get_current_ip():
    hostname = socket.gethostname()  # 获取主机名
    ip_address = socket.gethostbyname(hostname)  # 根据主机名获取 IP 地址
    return ip_address


def get_uuid():
    return str(uuid.uuid4())


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT)
