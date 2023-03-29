"""The user route"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from db.db_user import create_user
from schemas.user_schema import UserRequest, UserResponse


user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.get(
    "/",
    response_model=UserResponse
)
async def create_new_user(
    _request: UserRequest,
    _db: Session = Depends(get_db)
):
    """An endpoint to create a new user

    Args:
        _request (UserRequest): The new user data
        _db (Session, optional): The database session. Defaults to Depends(get_db).
    """
    create_user(_db, _request)
