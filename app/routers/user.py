from fastapi import status, HTTPException, Depends, APIRouter
from .. import models
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas import UserCreate, UserReturn
from .. import utils

router = APIRouter()

# Create a user
@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=UserReturn)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Hash the password
    hashed_pw = utils.hash(user.password)
    user.password = hashed_pw

    # Store user
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/user/{id}", response_model=UserReturn)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist.")

    return user