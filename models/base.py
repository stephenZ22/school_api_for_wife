from sqlalchemy.orm import DeclarativeBase,sessionmaker

from sqlalchemy import create_engine

engine = create_engine("sqlite:///school.db",echo=True,connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass