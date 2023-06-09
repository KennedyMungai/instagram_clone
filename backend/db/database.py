"""The database connection code"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_URL = "sqlite:///./ig_api.db"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    """The database connection code

    Yields:
        connection: The database connection
    """
    _db = SessionLocal()
    try:
        yield _db
    finally:
        _db.close()
