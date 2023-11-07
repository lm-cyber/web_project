import uvicorn
from api import app
from fastapi import File, UploadFile
from typing import Annotated


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
