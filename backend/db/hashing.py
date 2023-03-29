"""The file is going to contain the hashing logic"""
from passlib.context import CryptContext


password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash():
    """The hashing class"""
    def password_hash(_password: str):
        return password_context.hash(_password)
