<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0078D7&height=220&section=header&text=Student%20Management%20System&fontSize=45&animation=fadeIn&fontAlignY=38&desc=Smart%20%7C%20Fast%20%7C%20Reliable&descAlignY=55&descAlign=62" alt="Student Management System Header" width="100%"/>

<p>
<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/Maintained%3F-Yes-lightgrey?style=for-the-badge" />
</p>

<br>

<h3>A robust <b>Command Line Interface (CLI)</b> tool designed to streamline<br> student record management for educational institutions.</h3>

<p>
<a href="#-features">Features</a> •
<a href="#-installation">Installation</a> •
<a href="#-project-structure">Structure</a> •
<a href="#-developer">Developer</a>
</p>

</div>

---

## 🧐 About The Project

This **Student Management System** was developed during my **Python Developer Internship**. It serves as a practical demonstration of backend logic, database connectivity, and modular programming. It completely replaces manual file-keeping with a persistent, searchable, and secure **SQLite** database.

### 🛠️ Built With

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,sqlite,vscode,git" />
</div>

---

## ⚡ Features

| 🟢 Operation | 📝 Description |
| :--- | :--- |
| **Create** | Register new students with Name, Course, Email, and Contact validation. |
| **Read** | View the entire student database in a clean, formatted table. |
| **Search** | Instant lookup mechanism to find students by their unique `ID`. |
| **Update** | *(Future Scope)* Edit existing student details. |
| **Delete** | Remove specific records or wipe the database for a fresh start. |

---

## 📂 Project Structure

The project follows a modular architecture for easy maintenance and readability.

```text
Smart-Student-Management-System/
│
├── main.py                # 🚀 Main Entry Point (Menu Logic)
├── database.py            # ⚙️ Backend (SQL Connection & Queries)
├── view_student.py        # 📊 Frontend (Data Presentation Logic)
├── student.db             # 🗄️ Database (Auto-generated Storage)
└── README.md              # 📄 Documentation

