from pydantic import BaseModel


class ModelCreate(BaseModel):
    video_url : str
    callback_url: str