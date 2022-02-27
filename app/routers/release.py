from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas import ReleaseCreate, Return, Token
from typing import List, Optional
from .. import oauth2, models


router = APIRouter(
    prefix="/release",
    tags=['Releases']
)

@router.get("/api/health-check")
def health_check(db: Session = Depends(get_db)):
    return {"status": "healthy"}

# Get all releases
@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Return])
def get_releases(db: Session = Depends(get_db), user_id = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    print(limit)
    releases = db.query(models.Release).filter(models.Release.name.contains(search)).order_by(models.Release.release_date).limit(limit).offset(skip).all()
    return releases


# Get Release by ID - IDs are unique
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Return)
def get_post_by_id(id: int, db: Session = Depends(get_db), user_id = Depends(oauth2.get_current_user)):
    release = db.query(models.Release).filter(models.Release.id == id).first()
    
    if not release:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HTTP 404 Error: Post Not Found")
    
    return release

# Create a release
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_post(release: ReleaseCreate, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    new_release = models.Release(owner_id=current_user.id, **release.dict())
    db.add(new_release)
    db.commit()
    db.refresh(new_release)

    return new_release

# Delete Release by ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def del_post_by_id(id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    release_query = db.query(models.Release).filter(models.Release.id == id)
    release = release_query.first()

    #userid = current_user.id
    #releaseid = release.owner_id
    #print(userid, releaseid)
    #print(type(userid), type(releaseid))
    #print(userid == releaseid)

    if release == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HTTP 404 Error: Post Not Found")

    # still trying to figure out why current_user.id returns type str
    if release.owner_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action.")

    release_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update Release (shouldn't be used often...)
@router.put("/{id}", response_model=Return)
def update_post(id: int, updated_release: ReleaseCreate, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    release_query = db.query(models.Release).filter(models.Release.id == id)
    release = release_query.first()

    if release == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HTTP 404 Error: Post Not Found")

    # still trying to figure out why current_user.id returns type str
    if release.owner_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action.")
    
    release_query.update(updated_release.dict(), synchronize_session=False)
    db.commit()

    return release_query.first()
