from typing import Any

from pydantic import BaseModel

class CodeRequest(BaseModel):
    code: str

class ExceptionModel(BaseModel):
    name: str
    output: str

class ResponseModel(BaseModel):
    output: str

class BaseResponse(BaseModel):
    success: bool = True
    message: str | None = None
    type: str
    data: ExceptionModel | ResponseModel | None = None