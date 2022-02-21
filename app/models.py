from sqlalchemy import TIMESTAMP, Column, Integer, String, text
from .database import Base

class Release(Base):
    __tablename__ = "releases"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    release_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    dependency = Column(Integer, nullable=True, server_default='0')