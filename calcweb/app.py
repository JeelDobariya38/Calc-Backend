from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from . import metadata
from .core import core_router

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

@app.get("/heath", tags=["Internal"])
def health():
    return "Healthy!!"

app.include_router(core_router)

app.mount("/", StaticFiles(directory=metadata.WEBSITE_DIR_PATH, html=True), name="website")
