from fastapi import FastAPI, Response, status, HTTPException, Depends
from . import models
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .schemas import Release

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# **ROUTES BELOW**

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

# Get Release by ID - IDs are unique
@app.get("/release/{id}")
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    release = db.query(models.Release).filter(models.Release.id == id).first()
    
    if not release:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HTTP 404 Error: Post Not Found")
    
    return {"data": release}

# Delete Release by ID
@app.delete("/release/{id}")
def del_post_by_id(id: int, db: Session = Depends(get_db)):
    release = db.query(models.Release).filter(models.Release.id == id)

    if release.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HTTP 404 Error: Post Not Found")

    release.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update Release (shouldn't be used often...)
@app.put("/release/{id}")
def update_post(id: int, updated_release: Release, db: Session = Depends(get_db)):
    release_query = db.query(models.Release).filter(models.Release.id == id)
    release = release_query.first()

    if release == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HTTP 404 Error: Post Not Found")
    
    release_query.update(updated_release.dict(), synchronize_session=False)
    db.commit()
    return {"data": release_query.first()}