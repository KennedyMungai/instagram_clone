"""The file will hold the schema logic for the user"""
from pydantic import BaseModel


class UserBase(BaseModel):
    """The base model for the user data

    Args:
        BaseModel (Class): The parent class
    """
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    """The template for user response data

    Args:
        BaseModel (Class): The parent class
    """
    username: str
    email: str

    class Config:
        """The configuration class for the UserResponse class
        """
        orm_mode = True


class UserRequest(UserBase):
    """The template for the user response data

    Args:
        UserBase (Class): The parent class
    """


class User(BaseModel):
    username: str

    class Config:
        orm_mode = True
