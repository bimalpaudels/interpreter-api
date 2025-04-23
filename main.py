from fastapi import FastAPI, status
from starlette.responses import JSONResponse

from service import execution_flow
from model import CodeRequest

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/execute-code")
async def execute_code(code: CodeRequest):
    response = execution_flow(code.model_dump())
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
