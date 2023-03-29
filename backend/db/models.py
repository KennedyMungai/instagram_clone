"""File holds the db models for the app"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

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
    items = relationship('Post', back_populates='user')


class Post(Base):
    """The model for the Posts table

    Args:
        Base (Class): An instance declarative base
    """
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"))
    user = relationship('users', back_populates='items')
