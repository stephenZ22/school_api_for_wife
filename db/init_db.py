import sqlite3

def init_db():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Create the students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # Create the teachers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT,
            gender INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')

    conn.commit()
    conn.close()