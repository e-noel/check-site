from typing import Optional
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

class ReleaseCreate(ReleaseBase):
    pass

# Model for responses
class Return(ReleaseBase):
    release_date: datetime
    id: int
    owner_id: int

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

# User login schema
class Login(BaseModel):
    email: EmailStr
    password: str

# Token schema
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]

