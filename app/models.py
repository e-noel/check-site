from tkinter import CASCADE
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text, Boolean
from .database import Base

# Releases table
class Release(Base):
    __tablename__ = "releases"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    release_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    dependency = Column(Integer, nullable=True, server_default='0')
    is_archived = Column(Boolean, nullable=False, server_default='False')
    owner_id = Column(Integer, ForeignKey("users.id", ondelete=CASCADE), nullable=False)

# Users table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))