#!/usr/bin/python
"""an entry point to flask app"""
from flask import Flask, render_template, request
from utl import read_student, write_student, verification

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    return "Hello World"

@app.route("/login", methods=[ "POST", "GET"], strict_slashes=False)
def login():
    username= request.form.get("username")
    password= request.form.get("password")
    res= {}
    if username and password:
        if verification(Username=username, Password=password):
            res['message'] = "student login sucessful"
        else:
            res['message'] = "student not found"
    return render_template("login.html",data=res)

@app.route("/signup", methods={"POST", "GET"}, strict_slashes=False)
def register():
    email = request.form.get("email")
    username = request.form.get("username")
    fullname = request.form.get("fullname")
    password = request.form.get("password")
    res = {}
    if email and username and fullname and password:
        if read_student(Email=email, Username=username):
            res["message"] = "student already exists"
        else:
            write_student(Email=email, Username=username, Fullname=fullname, Password=password)
            res["message"] = "student created sucessfully"

    return render_template("signup.html", data=res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)