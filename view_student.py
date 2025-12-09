from database import create_connection


def view_all_students():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT student_id, name, course, semester, email, contact FROM students"
    )
    rows = cursor.fetchall()

    if not rows:
        print("No students found in database.")
    else:
        print("\nAll Students:\n")

        # Table header
        header = f"{'ID':<4} {'Name':<20} {'Course':<12} {'Semester':<9} {'Email':<25} {'Contact':<12}"
        line = "-" * len(header)
        print(header)
        print(line)

        # Each student row
        for row in rows:
            student_id, name, course, semester, email, contact = row
            print(
                f"{str(student_id):<4} "
                f"{name[:20]:<20} "
                f"{course[:12]:<12} "
                f"{semester[:9]:<9} "
                f"{email[:25]:<25} "
                f"{contact[:12]:<12}"
            )

        print(line)

    conn.close()
