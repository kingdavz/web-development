#!/usr/bin/python
"""A module that can read a file"""
import csv
import os
from datetime import datetime

CSV_FILE = "students.csv"
FIELDNAMES = ["username", "email", "fullname", "password"]

BLOGS_CSV = "blogs.csv"
BLOG_FIELDS = ["id", "title", "content", "author", "created_at"]



def _load_blogs():
    """load all blog rows from the csv. returns a list of dicts."""
    if not os.path.exists(BLOGS_CSV):
        return[]
    with open(BLOGS_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def _save_blogs(rows):
    """overwrite the bblogs in the CSV with the given list of blog dicts"""
    with open(BLOGS_CSV,'w', newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames=BLOG_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

def get_all_blogs():
    """return all logs sorted newest first."""
    blogs = _load_blogs()
    return sorted(blogs, key=lambda b: b.get("created_at", ""), reverse=True)

def get_blog_by_id(blog_id):
    """ return a single log dict matching the blog id, or none"""
    for blog in _load_blogs():
        if blog["id"] == str(blog_id):
            return blog
    return None

def create_blog(title, content, author):
    """append a new blog post to the csv. returns the new log dict"""
    blogs = _load_blogs()
    existing_ids = [int([b"id"]) for b in blogs if b["id"].isdigit()]
    new_id = max(existing_ids, default=0) + 1
    blog = {
        "id": str(new_id),
        "title": title.strip(),
        "content": content.strip(),
        "author": author.strip(),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    blogs.append(blog)
    _save_blogs(blogs)
    return blog

def delete_blog(blog_id, author):
    """delete a blog by id  only suceeds when calling author matches.
    returns from onsucess, false if not owner"""
    blogs = _load_blogs()
    original_len = len(blogs)
    blogs = [
        b for b in blogs
        if not (b["id"] == str(blog_id) and b["author"].strip().lower() == author.strip().lower())
    ]
    if len(blogs) < original_len:
        _save_blogs(blogs)
        return True
    return False

def get_blogs_by_author(author):
    """return all logs written by the given author. newest-first"""
    blogs = [b for b in _load_blogs() if b["author"].strip().lower() == author.strip().lower()]
    return sorted(blogs, key=lambda b: b.get("created_at", ""), reverse=True)







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
    

    