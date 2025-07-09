from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from typing import Optional
from sqlalchemy.orm import Session

from .base import Base, engine

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    gender: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, age={self.age}, gender={self.gender}, email={self.email})"

    @classmethod
    def with_name(cls, name: str):
        with Session(engine) as session:
            return session.query(cls).filter_by(name=name).first()

    @classmethod
    def with_id(cls, student_id: int):
        with Session(engine) as session:
            # Use the session to query the database
            return session.query(cls).filter_by(id=student_id).first()

    @classmethod
    def with_email(cls, email: str):
        with Session(engine) as session:
            return session.query(cls).filter_by(email=email).first()

    @classmethod
    def all_students(cls):
        with Session(engine) as session:
            return session.query(cls).all()