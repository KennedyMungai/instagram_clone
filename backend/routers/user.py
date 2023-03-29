"""The user route"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from backend.db.database import get_db
from backend.schemas.user_schema import UserRequest, UserResponse


user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.get("/", response_model=UserResponse)
async def create_user(_request: UserRequest, _db: Session = Depends(get_db)):
    pass
