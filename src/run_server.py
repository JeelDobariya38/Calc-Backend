from src.main import warning
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

if __name__ == "__main__":
    environment = os.getenv("ENVIRONMENT")
    if environment == "Development":
        warning()

    host = os.getenv("HOST")
    port = os.getenv("PORT")

    if not host:
        host = "127.0.0.1"

    if not port:
        port = 8080

    try:
        uvicorn.run("calcweb:app", host=host, port=int(port), log_level="info")
    except KeyboardInterrupt:
        print("Quitting the server!!!")
