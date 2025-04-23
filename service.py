from restricted.helpers import execute_restricted
from model import BaseResponse, ExceptionModel, ResponseModel


def execution_flow(code):
    try:
        response = execute_restricted(code.get('code'))
        return BaseResponse(
            data=ResponseModel(output=response),
            success=True,
            type="normal",
        ).model_dump()
    except Exception as e:
        response = ExceptionModel(
            name=e.__class__.__name__,
            output=str(e)
        )
        return BaseResponse(
            data=response,
            success=True,
            type="exception"
        ).model_dump()

