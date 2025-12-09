import sqlite3


def create_connection():
    # Connects (or creates) the SQLite database file
    conn = sqlite3.connect("student.db")
    return conn


def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            semester TEXT NOT NULL,
            email TEXT,
            contact TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_student(name, course, semester, email, contact):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (name, course, semester, email, contact)
        VALUES (?, ?, ?, ?, ?)
    """, (name, course, semester, email, contact))

    conn.commit()
    conn.close()


def search_student_by_id(student_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT student_id, name, course, semester, email, contact FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()
    conn.close()
    return student


def delete_student_by_id(student_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    conn.commit()

    rows_deleted = cursor.rowcount  # how many rows were removed
    conn.close()
    return rows_deleted


def delete_all_students():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students")
    conn.commit()

    rows_deleted = cursor.rowcount
    conn.close()
    return rows_deleted
