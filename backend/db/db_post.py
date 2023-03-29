"""Determines all the Post interactions with the database"""
from datetime import datetime

from db.models import Post
from schemas.post_schema import PostRequest
from sqlalchemy.orm.session import Session


def create_post(_request: PostRequest, _db: Session):
    new_post = Post(
        mage_url=_request.image_url,
        image_url_type=_request.image_url_type,
        caption=_request.caption,
        timestamp=datetime.utcnow(),
        user_id=_request.creator_id
    )
