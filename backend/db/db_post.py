"""Determines all the Post interactions with the database"""
from schemas.post_schema import PostRequest
from sqlalchemy.orm.session import Session
from db.models import Post


def create_post(_request: PostRequest, _db: Session):
    pass
