"""The file is going to contain the hashing logic"""
from passlib.context import CryptContext


password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
