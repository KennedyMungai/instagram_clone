"""The file that communicates with the database"""
from db.hashing import password_hash
from schemas.user_schema import UserRequest
from sqlalchemy.orm.session import Session

from .models import User


def create_user(_db: Session, _request: UserRequest):
    """The create user function

    Args:
        _db (Session): The database session
        _request (UserRequest): The template for the user request data
    """
    _new_user = User(
        username=_request.username,
        email=_request.email,
        password=password_hash(hash, _request.password)
    )

    _db.add(_new_user)
    _db.commit()
    _db.refresh(_new_user)

    return _new_user
