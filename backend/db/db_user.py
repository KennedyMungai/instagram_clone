"""The file that communicates with the database"""
from sqlalchemy.orm.session import Session
from schemas.user_schema import UserRequest


def create_user(_db: Session, request: UserRequest):
    pass
