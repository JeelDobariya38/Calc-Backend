from fastapi import APIRouter, Response, status
from calc import calc_execute
from calc.customerr import CalcException

from .model import Command

core_router = APIRouter()

@core_router.post("/execute", tags=["Calc"])
def execute(_command: Command, response: Response):
    try:
        res = calc_execute(_command.command)
    except CalcException as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error": e}
    return {"command": _command.command, "result": res}
