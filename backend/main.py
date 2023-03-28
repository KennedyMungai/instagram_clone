"""The main entry point for the project"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root() -> str:
    """The root API endpoint

    Returns:
        str: A message is returned after successful execution
    """
    return "API works"
