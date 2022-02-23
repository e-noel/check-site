from pydantic import BaseModel

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
class Return(BaseModel):
    name: str
    dependency: int
    is_archived: bool

    class Config:
        orm_mode = True