#!/usr/bin/python
"""an entry point to flask app"""
from flask import Flask, render_template, request, redirect
from utl import read_student, write_student, verification, change
from uuid import uuid4

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

@app.route("/signup", methods=["POST", "GET"], strict_slashes=False)
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

@app.route("/forgotpassword", methods=["POST", "GET"], strict_slashes=False)
def forgot_password():
    username= request.form.get("username")
    res = {}
    if username:
        if change(Username=username):
            return redirect(f'/change/{str(uuid4())}/{username}')
        else:
            res["message"] = "student not found"

    return render_template("password.html", data=res)

@app.route("/change/:token/:username", methods=["GET", "POST"], strict_slashes=False)
def new_password(token,username):
    res = {}
    print(token, username)
    return render_template("newpass.html", data=res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)