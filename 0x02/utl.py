#!/usr/bin/python
"""A module that can read a file"""
import csv
import os

CSV_FILE = "students.csv"
FIELDNAMES = ["username", "email", "fullname", "password"]

def _load_students():
    """load all atudents rows from the Csv. Returns a list of dicts"""
    if not os.path.exists(CSV_FILE):
        return[]
    with open(CSV_FILE, "r", encoding= "utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def _save_students(rows):
    """overite csv with given list of student dicts"""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

def verification(username, email):
    """a function that verifies content in a file"""
    students = _load_students()
    for row in students:
        if row["username"].strip().lower() == username.strip().lower():
            return True
        if row["email"].strip().lower() == email.strip().lower():
            return True
    return False

def read_students(username, password):
    """Authenticate a student. Return true if usernam and password match."""
    if not username or not password:
        return False
    students = _load_students()
    for row in students:
        if(row["username"].strip().lower() == username.strip().lower()
           and row["password"].strip().lower() == password.strip()):
            return True
        return False
    
def get_student(username):
    """return the student dict for yhe given username, or none if not found."""
    if not username:
        return None
    students = _load_students()
    for row in students:
        if row["username"].strip().lower() == username.strip().lower():
            return row
    return None

def write_student(username, email, fullname, password):
    """Append a new student record to csv file"""
    students = _load_students()
    students.append({
        "username": username.strip(),
        "email": email.strip(),
        "fullname": fullname.strip(),
        "password": password.strip()
    })
    _save_students(students)
    return True
            
    

def update_password(username, newpassword):
    """a function that updates  the username and password"""
    students = _load_students()
    updated = False
    for row in students:
        if row["username"].strip().lower() == username.strip().lower():
            row["password"] =  newpassword.strip()
            updated = True
            break
    if updated:
        _save_students(students)
    return updated
    

    