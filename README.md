<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0078D7&height=220&section=header&text=Student%20Management%20System&fontSize=45&animation=fadeIn&fontAlignY=38&desc=Smart%20%7C%20Fast%20%7C%20Reliable&descAlignY=55&descAlign=62" width="100%" />

<p>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Maintained-Yes-lightgrey?style=for-the-badge" />
</p>

<br/>

<h3>
A robust <b>Command Line Interface (CLI)</b> application designed to streamline<br>
student record management for educational institutions.
</h3>

<p>
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-developer">Developer</a>
</p>

</div>

---

## 🧐 About The Project

The **Student Management System** was developed during my **Python Developer Internship**.  
It demonstrates **backend logic**, **database connectivity**, and **modular programming** concepts using Python.

This system replaces manual record keeping with a **persistent, searchable, and secure SQLite database**, allowing fast and reliable student data management.

---

## 🛠️ Built With

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,sqlite,vscode,git" />
</div>

---

## ⚡ Features

| 🟢 Operation | 📝 Description |
|------------|---------------|
| **Create** | Register new students with Name, Course, Email, and Contact validation |
| **Read** | View all student records in a clean, formatted table |
| **Search** | Quickly find students using their unique **Student ID** |
| **Update** | *(Future Scope)* Modify existing student details |
| **Delete** | Delete individual records or wipe all data for a fresh start |

---

## 🧩 Database Schema

| Column Name | Data Type | Constraints |
|------------|----------|-------------|
| student_id | INTEGER | Primary Key, Auto Increment |
| name | TEXT | NOT NULL |
| course | TEXT | NOT NULL |
| semester | TEXT | NOT NULL |
| email | TEXT | UNIQUE |
| contact | TEXT | — |

---

## 💻 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nirbhay-kachhadiya/Smart-Student-Management-System.git
Project Overview