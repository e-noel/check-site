from fastapi import FastAPI, Response, status, HTTPException, Depends
from . import models
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Schema
class Release(BaseModel):
    name: str
    dependency: int = "0"
    is_archived: bool = False

# Route for checking db connection health
@app.get("/api/health-check")
def health_check(db: Session = Depends(get_db)):
    return {"status": "healthy"}

# Get all releases
@app.get("/release")
def get_releases(db: Session = Depends(get_db)):
    releases = db.query(models.Release).all()
    return {"data": releases}

# Add a release
@app.post("/release")
def add_post(release: Release, db: Session = Depends(get_db)):
    new_release = models.Release(**release.dict())
    db.add(new_release)
    db.commit()
    db.refresh(new_release)

    return {"data": new_release}
