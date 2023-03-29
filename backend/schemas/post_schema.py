"""The post schema file"""
from pydantic import BaseModel


class PostBase(BaseModel):
    """The base class for the Post data

    Args:
        BaseModel (Class): The parent claSS
    """
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int
