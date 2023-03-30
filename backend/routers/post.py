"""The Post router file"""
from db.database import get_db
from fastapi import APIRouter, Depends, status, HTTPException
from schemas.post_schema import PostRequest
from sqlalchemy.orm.session import Session

post_router = APIRouter(prefix="/post", tags=["Post"])


image_url_types = ['absolute', 'relative']


@post_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_post(_request: PostRequest, _db: Session = Depends(get_db)):
    if not _request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Parameter image url type can only take the values 'absolute' or 'relative'"
        )
