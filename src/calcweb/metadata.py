from pathlib import Path

TITLE = "Calc - Math Interpreter"
DESCRIPTION = """
Calc API helps you do math related stuff. 🚀
"""
VERSION = "0.2.0"
LICENSE_INFO = {
    "name": "MIT",
    "identifier": "MIT",
}
METADATA_TAGS = [
    {
        "name": "Calc",
        "description": "Use for Interacting with Calc App",
        # "externalDocs": {
        #     "description": "Calc Docs",
        #     "url": "https://fastapi.tiangolo.com/",
        # },
    },
    {
        "name": "Internal",
        "description": "use for specific purpose",
    }
]
WEBSITE_DIR_PATH = Path(__file__).parent.joinpath("./website")
