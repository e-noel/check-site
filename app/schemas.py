from pydantic import BaseModel

# Pydantic Model (Schema)
class Release(BaseModel):
    name: str
    dependency: int = "0"
    is_archived: bool = False