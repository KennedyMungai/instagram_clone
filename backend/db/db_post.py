"""Determines all the Post interactions with the database"""
from db.models import Post
from schemas.post_schema import PostRequest
from sqlalchemy.orm.session import Session


def create_post(_request: PostRequest, _db: Session):
    pass
