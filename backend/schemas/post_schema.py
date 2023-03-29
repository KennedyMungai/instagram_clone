"""The post schema file"""
from datetime import datetime

from pydantic import BaseModel

from backend.schemas.user_schema import User


class PostBase(BaseModel):
    """The base class for the Post data

    Args:
        BaseModel (Class): The parent claSS
    """
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


class PostResponse(BaseModel):
    """The template for teh Post response data

    Args:
        BaseModel (Class): The parent class
    """
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User

    class Config:
        """The configuration subclass"""
        orm_mode = True
