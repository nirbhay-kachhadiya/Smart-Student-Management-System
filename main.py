from database import (
    insert_student,
    create_table,
    search_student_by_id,
    delete_student_by_id,
    delete_all_students,
)
from view_student import view_all_students


# ------------ Input Validation Helpers ------------

def is_valid_email(email: str) -> bool:
    """
    Very simple email validation:
    - must contain '@'
    - must contain '.'
    """
    return "@" in email and "." in email


def is_valid_contact(contact: str) -> bool:
    """
    Contact number validation:
    - only digits
    - exactly 10 digits
    """
    return contact.isdigit() and len(contact) == 10


# ------------ Main Features ------------

def add_student():
    print("\n--- Add New Student ---")

    name = input("Enter Name: ")
    course = input("Enter Course: ")
    semester = input("Enter Semester: ")

    # Email validation loop
    while True:
        email = input("Enter Email: ")
        if is_valid_email(email):
            break
        print("❌ Invalid email format. Please try again (example: abc@gmail.com).")

    # Contact validation loop
    while True:
        contact = input("Enter Contact (10 digits): ")
        if is_valid_contact(contact):
            break
        print("❌ Invalid contact number. Please enter exactly 10 digits (only numbers).")

    insert_student(name, course, semester, email, contact)
    print("\n✅ Student record added successfully")


def search_student():
    print("\n--- Search Student by ID ---")

    student_id = input("Enter Student ID: ")

    student = search_student_by_id(student_id)

    if student:
        sid, name, course, semester, email, contact = student

        # Table-style display for single student
        print("\n✅ Student Found\n")
        header = f"{'ID':<4} {'Name':<20} {'Course':<12} {'Semester':<9} {'Email':<25} {'Contact':<12}"
        line = "-" * len(header)
        print(header)
        print(line)
        print(f"{str(sid):<4} {name[:20]:<20} {course[:12]:<12} {semester[:9]:<9} {email[:25]:<25} {contact[:12]:<12}")
        print(line)
    else:
        print("\n❌ No student found with this ID.")


def delete_student():
    print("\n--- Delete Single Student ---")

    student_id = input("Enter Student ID to delete: ")

    student = search_student_by_id(student_id)

    if not student:
        print("\n❌ No student found with this ID. Nothing to delete.")
        return

    sid, name, course, semester, email, contact = student
    print("\nStudent to be deleted:")
    print(f"ID: {sid}")
    print(f"Name: {name}")
    print(f"Course: {course}")
    print(f"Semester: {semester}")
    print(f"Email: {email}")
    print(f"Contact: {contact}")

    confirm = input("\nAre you sure you want to delete this student? (y/n): ").strip().lower()

    if confirm == "y":
        rows_deleted = delete_student_by_id(student_id)
        if rows_deleted > 0:
            print("\n✅ Student record deleted successfully")
        else:
            print("\n⚠ Something went wrong. Record not deleted.")
    else:
        print("\n❎ Delete cancelled.")


def delete_all():
    print("\n--- Delete ALL Students ---")
    confirm = input(
        "⚠ This will remove ALL records permanently. Are you sure? (type 'DELETE' to confirm): "
    ).strip()

    if confirm != "DELETE":
        print("\n❎ Delete all cancelled.")
        return

    rows_deleted = delete_all_students()

    if rows_deleted > 0:
        print(f"\n✅ Deleted {rows_deleted} student record(s) from database.")
    else:
        print("\nℹ No records to delete. Database is already empty.")


def main():
    create_table()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Delete Single Student")
        print("5. Delete ALL Students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            delete_all()
        elif choice == "6":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
