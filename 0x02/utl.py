#!/usr/bin/python
"""A module that can read a file"""
import csv
import os

def read_student(data):
    """a function that read student data from csv file"""
    try:
        with open("students.csv", "r", encoding= "utf-8 ") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["email"] == data.get("email").strip():
                    return True
        return False
    except FileNotFoundError:
        return False
    
def write_student(data):
    """A function that write student data into csv file"""
    try:
        with open("students.csv", "w+", encoding="utf-8") as f:
            fieldnames = data.keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)
    except Exception:
        with open("students.csv", "a") as f:
            f.write(data.decode("utf-8") + "\n")
    return True