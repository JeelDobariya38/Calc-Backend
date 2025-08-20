from fastapi import FastAPI, Response, status
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from calccli import calc_execute
from src.calc.customerr import CalcException
from .model import Command
from . import metadata


app = FastAPI(
    title=metadata.TITLE,
    description=metadata.DESCRIPTION,
    version=metadata.VERSION,
    license_info=metadata.LICENSE_INFO,
    openapi_tags=metadata.METADATA_TAGS,
)

origins = [
    "http://localhost",
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/", tags=["Frontend"])
def root():
    return FileResponse("website/index.html")


@app.get("/style.css", tags=["Frontend"])
def style():
    return FileResponse("website/style.css")


@app.get("/script.js", tags=["Frontend"])
def script():
    return FileResponse("website/script.js")


@app.get("/heath", tags=["Internal"])
def health():
    return "Healthy!!"


@app.post("/execute", tags=["Calc"])
def execute(_command: Command, response: Response):
    try:
        res = calc_execute(_command.command)
    except CalcException as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error": e}
    return {"command": _command.command, "result": res}
