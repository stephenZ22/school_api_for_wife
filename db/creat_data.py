import sqlite3
import models.students as students_model
import models.base as db_engine
from sqlalchemy.orm import Session

def create_student_by_orm(name: str, gender: int, age: int = 7, email: str = ''):
    try:
        with Session(db_engine.engine) as session:
            student = students_model.Student(name=name, age=age, gender=gender, email=email)
            session.add(student)
            session.commit()
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True

def create_students(name: str, gender: int, age: int = 7, email: str = ''):
    conn = sqlite3.connect('school.db', timeout=3)
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (name, age, gender,email) VALUES (?, ?, ?, ?)
        ''', (name, age, gender,email))

        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
        return False
    except sqlite3.OperationalError as e:
        print(f"Operational Error: {e}")
        return False
    finally:
        conn.close()
    
    return True

def create_teachers(name: str, age: int, gender: int):
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO teachers (name, age, gender) VALUES (?, ?, ?)
    ''', (name, age, gender))

    conn.commit()
    conn.close()

def create_courses(name: str, description: str):
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO courses (name, description) VALUES (?, ?)
    ''', (name, description))

    conn.commit()
    conn.close()
