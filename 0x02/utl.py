#!/usr/bin/python
"""A module that can read a file"""
import csv
import os

def read_student(**kwargs):
    """a function that read student data from csv file"""
    try:
        with open("students.csv", "r", encoding= "utf-8 ") as f:
            reader = csv.DictReader(f)
            for row in reader:
        
                if row['Email'] == kwargs['Email'] or row['Username'] == kwargs['Username']:
                    return True
        return False
    except FileNotFoundError:
        return False
    
def write_student(**kwargs):
    """A function that write student data into csv file"""
    try:
        with open("students.csv", "w+", encoding="utf-8") as f:
            fieldnames = kwargs.keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(kwargs)
    except Exception:
        with open("students.csv", "a") as f:
            f.write(kwargs)
    return True

def verification(**kwargs):
    """a function that verifies content in a file"""
    try:
        with open("students.csv", "r", encoding= "utf-8 ") as f:
            reader = csv.DictReader(f)
            for row in reader:
            
                if row['Username'] == kwargs['Username'] and row['Password'] == kwargs['Password']:
                    return True
        return False
    except FileNotFoundError:
        return False
    
def change(**kwargs):
    """A function that changes the password in a file"""
    try:
        with open("students.csv", "r", encoding= "utf-8 ") as f:
            reader = csv.DictReader(f)
            for row in reader:
            
                if row['Username'] == kwargs['Username']:
                    return True
        return False
    except FileNotFoundError:
        return False

    