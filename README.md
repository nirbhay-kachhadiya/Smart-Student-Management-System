# 🎓 Student Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

A simple, robust, and menu-driven **Student Management System** developed as part of a **Python Developer Internship**. This project demonstrates complete **CRUD operations** (Create, Read, Update, Delete) on student records using a clean, modular code structure and a secure SQLite database.

---

## 📌 Project Overview

The **Smart Student Management System** is designed to manage student records efficiently through a console-based interface. It eliminates manual data handling errors and provides a persistent storage solution using SQLite.

**Key Capabilities:**
* Add and validate new student details.
* View all registered students in a tabular format.
* Search for specific students by their unique ID.
* Securely delete records (single or bulk deletion).

---

## 🚀 Key Features

| Feature | Description |
| :--- | :--- |
| ✅ **Add Records** | Capture student Name, Course, Semester, Email, and Contact info. |
| ✅ **View Records** | Fetch and display all data from the database instantly. |
| ✅ **Search Function** | Locate specific students using their `Student ID`. |
| ✅ **Delete Function** | Remove a single student or wipe the entire database with confirmation. |
| ✅ **Data Persistence** | Uses `sqlite3` to store data permanently in `student.db`. |
| ✅ **Modular Design** | Code is split into logical files (`main.py`, `database.py`, etc.) for maintainability. |

---

## 🛠 Tech Stack

* **Language:** Python 3.x
* **Database:** SQLite 3
* **Standard Libraries:** `sqlite3`, `sys`, `os`
* **Development Environment:** VS Code / PyCharm

---

## 📂 Project Structure

```text
Smart-Student-Management-System/
│
├── main.py                # Main entry point (Menu-driven application)
├── database.py            # Handles database connections and SQL queries
├── view_student.py        # Logic to display formatted student records
├── student.db             # SQLite database file (Auto-generated)
└── README.md              # Project documentation

▶ How to Run the Project
Follow these steps to set up and run the project locally:

1️⃣ Clone the Repository
git clone [https://github.com/nirbhay-kachhadiya/Smart-Student-Management-System.git](https://github.com/nirbhay-kachhadiya/Smart-Student-Management-System.git)

2️⃣ Navigate to Project Directory

cd student-management-system

3️⃣ Run the Application

python main.py

💻 Application Menu Preview
When you run the application, you will see the following interactive menu:

===== Student Management System =====
1. Add Student
2. View All Students
3. Search Student by ID
4. Delete Single Student
5. Delete ALL Students
6. Exit
=====================================
Enter your choice:

🗃 Database Schema
The project uses a single table named students with the following structure:
### Database Table: students

| Column Name | Data Type | Constraints |
|------------|----------|-------------|
| student_id | INTEGER | Primary Key, Auto Increment |
| name | TEXT | NOT NULL |
| course | TEXT | NOT NULL |
| semester | TEXT | NOT NULL |
| email | TEXT | UNIQUE |
| contact | TEXT | — |

🎯 Learning Outcomes
By building this project during my internship, I gained hands-on experience in:

🐍 Python Fundamentals: Mastering loops, functions, and conditional logic.

🗄️ Database Management: Connecting Python to SQLite and executing SQL queries.

⚙️ CRUD Operations: Implementing Create, Read, Update, and Delete functionalities.

🧩 Modular Programming: Structuring code across multiple files for better organization.

🐞 Debugging: Handling errors and edge cases in user input. 

👨‍💻 Developer Info
Name: Nirbhay Kachhadiya

Role: Python Developer Intern

Course: BCA (Bachelor of Computer Applications)

College: Silver Oak College of Computer Application