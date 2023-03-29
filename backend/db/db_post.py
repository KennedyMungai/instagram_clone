"""Determines all the Post interactions with the database"""
from db.models import Post
from schemas.post_schema import PostResponse
from sqlalchemy.orm.session import Session
from datetime import datetime


def create_post(_request: PostResponse, _db: Session):
    new_post = Post(
        mage_url=_request.image_url,
        image_url_type=_request.image_url_type,
        caption=_request.caption,
        timestamp=datetime.utcnow(),
        user_id=_request.creator_id
    )
