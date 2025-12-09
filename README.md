# 🎓 Smart Student Management System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-orange)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

A **Python-based Command Line Student Management System** using **SQLite**.  
This project helps manage student records with options to **add, view, search, and delete students** through a simple menu-based interface.

🔗 **GitHub Repository:**  
https://github.com/nirbhay-kachhadiya/Smart-Student-Management-System  

---

## 📌 1. Project Overview

This project is developed as a **console-based application** for managing basic student data:

- Stores data in a local SQLite database (`student.db`)
- Focuses on **clean code**, **input validation**, and **basic DB operations**
- Suitable for:
  - Academic submission
  - Python + Database learning
  - Mini-project / portfolio project

---

## 🎯 2. Objectives

- Implement a **student record management system** using Python.
- Practice **CRUD operations** (Create, Read, Update, Delete) with SQLite.
- Use **modular programming** by separating logic into multiple files.
- Provide a **user-friendly terminal interface**.

---

## 📂 3. Project Structure

text
Smart-Student-Management-System/
├── main.py          # Main menu & application logic
├── database.py      # Database connection & CRUD operations
├── view_student.py  # Display student records in table format
└── student.db       # SQLite database (auto-created when running)

## 🛠️ 4. Technologies Used

Language: Python 3.x

Database: SQLite (sqlite3 module – built-in)

Editor (recommended): VS Code / PyCharm / Any IDE

Interface: Command Line Interface (CLI)

## 🚀 5. Features

➕ Add new student records

📋 View all students in a clean table format

🔍 Search student by ID

❌ Delete a single student by ID (with confirmation)

⚠ Delete all students (with strong confirmation)

✅ Input validation:

Email must contain @ and .

Contact must be 10 digits only

💾 Data is persisted in student.db (SQLite database)

## 📱 6. Mobile-Friendly & GitHub View Notes

This README is optimized for mobile and small screens:

Short paragraphs for easier reading

Bullet lists instead of very wide tables

Code blocks for commands and output

Sections clearly numbered for assignments/college reports

GitHub automatically makes code blocks and headings readable on mobile.

## 💻 7. How to Run (Step-by-Step)
7.1 Prerequisites

Install Python 3.8+

(Optional but recommended) Install VS Code + Python extension

Check Python version:
python --version
7.2 Clone the Repository
git clone https://github.com/nirbhay-kachhadiya/Smart-Student-Management-System.git
cd Smart-Student-Management-System
7.3 Run the Application
python main.py
(Use python3 main.py if required.)
🧭 8. Application Menu & Flow

When you run main.py, you’ll see:

===== Student Management System =====
1. Add Student
2. View All Students
3. Search Student by ID
4. Delete Single Student
5. Delete ALL Students
6. Exit
Enter your choice (1-6):


1 → Add new student

2 → View all students

3 → Search by student ID

4 → Delete a specific student

5 → Delete all records

6 → Exit application

🧪 9. Sample Outputs
9.1 Add Student
--- Add New Student ---
Enter Name: Nirbhay
Enter Course: BCA
Enter Semester: 5th
Enter Email: nirbhay@example.com
Enter Contact (10 digits): 9876543210

✅ Student record added successfully

9.2 View All Students
All Students:

ID   Name                 Course       Semester  Email                     Contact
------------------------------------------------------------------------------------
1    Nirbhay              BCA          5th       nirbhay@example.com       9876543210
2    Harsh                BCA          5th       harsh@example.com         9123456780
------------------------------------------------------------------------------------

9.3 Search by ID
--- Search Student by ID ---
Enter Student ID: 1

✅ Student Found

ID   Name                 Course       Semester  Email                     Contact
------------------------------------------------------------------------------------
1    Nirbhay              BCA          5th       nirbhay@example.com       9876543210
------------------------------------------------------------------------------------

9.4 Delete Single Student
--- Delete Single Student ---
Enter Student ID to delete: 1

Student to be deleted:
ID: 1
Name: Nirbhay
Course: BCA
Semester: 5th
Email: nirbhay@example.com
Contact: 9876543210

Are you sure you want to delete this student? (y/n): y

✅ Student record deleted successfully

🗄️ 10. Database Design

Database File: student.db
Table Name: students

CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL,
    course     TEXT NOT NULL,
    semester   TEXT NOT NULL,
    email      TEXT,
    contact    TEXT
);

✅ 11. Input Validation Details

Handled in main.py:

Email Validation (is_valid_email)

Must contain @

Must contain .

Contact Validation (is_valid_contact)

Only digits using .isdigit()

Length must be exactly 10

If invalid, the user is asked to re-enter the value until it is valid.

🎓 12. For College Submission (Theory Points)

You can mention the following points in your project report / viva:

Type of Project: Console-based Student Management System

Language Used: Python

Database Used: SQLite

Architecture:

main.py → Interface + input handling

database.py → Database connection & queries

view_student.py → Display logic

Concepts Demonstrated:

File structure & modular programming

Database CRUD operations

Basic input validation

Use of primary key (student_id)

You can also add screenshots of:

Application menu in terminal

Add student screen

View all students screen

Add a section in your report/README like:

## 📸 Screenshots

(You can paste screenshots here after uploading them to the repo.)

🖥️ 13. GUI Version – Future Plan (Roadmap)

You can mention this as Future Scope in college submission:

Planned features for a GUI-based version:

Technology Choice

Python GUI framework:

Tkinter (built-in & simple) or

PyQt / Kivy (advanced)

Proposed GUI Screens

Dashboard / Home Screen

Add Student Form (with text fields and buttons)

View Students Table (with scrollbars)

Search by ID (input box + result display)

Buttons for:

Add

View All

Search

Delete By ID

Delete All

Backend Reuse

Re-use existing functions:

insert_student()

search_student_by_id()

delete_student_by_id()

delete_all_students()

Only the front-end changes (CLI → GUI)

Extra GUI Features (Optional)

Dropdown for course/semester

Confirmation popups for delete operations

Success/error message boxes

You can write in report:

“Currently the system is CLI-based. In future, it can be extended to a GUI application using Tkinter/PyQt to make it more user-friendly.”

👨‍💻 14. Author

Nirbhay Kachhadiya
🔗 GitHub: @nirbhay-kachhadiya

📜 15. License

This project is currently for learning and educational purposes.

If you want, you can later add an MIT License by creating a file named LICENSE in the repository and updating this section.
