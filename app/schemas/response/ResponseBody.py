from typing import Any

from pydantic import BaseModel


class ResponseBody(BaseModel):
    code: int
    message: str
    data: Any = None
