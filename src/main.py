from app.blog.factory import create_blog
from fastapi import FastAPI

app = FastAPI()


@app.get("/checkhealth")
def checkhealth():
    return {"ping": "pong"}


blog_app = create_blog()
app.mount("/v1", blog_app)
