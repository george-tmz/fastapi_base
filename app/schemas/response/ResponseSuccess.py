from app.schemas.response.ResponseBody import ResponseBody


class ResponseSuccess(ResponseBody):
    code: int = 200
    message: str = "success"