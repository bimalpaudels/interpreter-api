from fastapi import FastAPI, status
from starlette.responses import JSONResponse

from config import configure_app, global_exception_handler
from service import execution_flow
from model import CodeRequest

app = FastAPI()
configure_app(app)
app.add_exception_handler(Exception, global_exception_handler)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/execute-code")
async def execute_code(code: CodeRequest):
    response = execution_flow(code.model_dump())
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
