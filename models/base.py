from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import create_engine

engine = create_engine("sqlite:///school.db")

class Base(DeclarativeBase):
    pass