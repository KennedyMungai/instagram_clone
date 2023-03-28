"""File holds the db models for the app"""
from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    """The model for the user table

    Args:
        Base (Class): A class instance that does stuff
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
