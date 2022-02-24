from email.policy import HTTP
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import release, user

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(release.router)
app.include_router(user.router)

@app.get("/")
def index():
    return {"message": "hello!"}