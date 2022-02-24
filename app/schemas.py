from pydantic import BaseModel, EmailStr
from datetime import datetime
# Pydantic Model (Schema)
""" class Release(BaseModel):
    name: str
    dependency: int = "0"
    is_archived: bool = False
 """

 # Creating a base model to extend to other classes
 # that may be used.
class ReleaseBase(BaseModel):
    name: str
    dependency: int = "0"
    is_archived: bool = False

    class Config:
        orm_mode = True

class Release(ReleaseBase):
    pass

# Model for responses
class Return(ReleaseBase):
    release_date: datetime

    class Config:
        orm_mode = True

# Model for users
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# User Response model
class UserReturn(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode=True