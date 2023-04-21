from typing import Dict

from fastapi import FastAPI

from app.blog.factory import create_blog_server

app = FastAPI()


@app.get("/checkhealth")
def checkhealth() -> Dict[str, str]:
    return {"ping": "pong"}


create_blog_server(app)
