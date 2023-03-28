"""The main entry point for the project"""
from db import models
from db.database import engine
from fastapi import FastAPI


models.Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
async def root() -> str:
    """The root API endpoint

    Returns:
        str: A message is returned after successful execution
    """
    return "API works"
