"""Determines all the Post interactions with the database"""
from datetime import datetime

from db.models import Post
from schemas.post_schema import PostRequest
from sqlalchemy.orm.session import Session


def create_post(_request: PostRequest, _db: Session):
    """A function that creates a new post

    Args:
        _request (PostRequest): The template for the Post request data
        _db (Session): The database session

    Returns:
        PostRequest: Te new post
    """
    _new_post = Post(
        mage_url=_request.image_url,
        image_url_type=_request.image_url_type,
        caption=_request.caption,
        timestamp=datetime.utcnow(),
        user_id=_request.creator_id
    )

    _db.add(_new_post)
    _db.commit()
    _db.refresh(_new_post)

    return _new_post
