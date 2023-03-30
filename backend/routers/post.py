"""The Post router file"""
from fastapi import APIRouter


post_router = APIRouter(prefix="/post", tags=["Post"])


image_url_types = ['absolute', 'relative']
