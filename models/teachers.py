from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, SmallInteger
from typing import Optional
from .base import Base, SessionLocal

class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[int] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    gender: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)

    def __repr__(self):
        return f"Teacher(id={self.id}, name={self.name}, age={self.age}, email={self.email}, gender={self.gender})"


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "gender": self.gender
        }
    
    @classmethod
    def create_teacher(cls, name: str, age: int, email: str, gender: Optional[str]):
            with SessionLocal() as session:
                try:

                    teacher = cls(name=name, age=age, email=email, gender=gender)
                    session.add(teacher)
                    session.commit()
                    session.refresh(teacher)
                    return teacher

                except Exception as e:
                    print(f"Error creating teacher: {e}")
                return None
    
        
    @classmethod
    def with_id(cls, teacher_id: int):
        with SessionLocal() as session:
            return session.query(cls).filter_by(id=teacher_id).first()

    @classmethod  
    def with_name(cls, name: str):
        with SessionLocal() as session:
            return session.query(cls).filter_by(name=name).first()
    
    @classmethod
    def with_email(cls, email: str):
        with SessionLocal() as session:
            return session.query(cls).filter_by(email=email).first()