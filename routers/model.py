from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.Models import Model
from app.schemas.ModelCreate import ModelCreate
from app.schemas.response.ResponseBody import ResponseBody
from app.schemas.response.ResponseSuccess import ResponseSuccess
from core.DbConnect import get_db
from utils import get_uuid, get_current_ip

router = APIRouter()


@router.post("/model", response_model=ResponseBody)
async def create_model(data: ModelCreate, db: Session = Depends(get_db)):
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
    return ResponseSuccess(data={"task_id": model.task_id, "status": model.status})
