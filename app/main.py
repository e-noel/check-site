from fastapi import FastAPI, Response, status, HTTPException, Depends
from . import models
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

#Example Route

@app.get("/api/health-check")
def test_posts(db: Session = Depends(get_db)):
    return {"status": "healthy"}
