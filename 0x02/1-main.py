#!/usr/bin/python
"""an entry point to flask app"""
from flask import Flask, render_template, request, redirect, url_for
from utl import read_students, write_student, verification, get_student, update_password

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    return "Hello World"

@app.route("/login", methods=[ "POST", "GET"], strict_slashes=False)
def login():
    res= {}
    if request.method == "POST":
        username= request.form.get("username","").strip()
        password= request.form.get("password","").strip()
   
        if not username or not password:
            res["message"] = "Username and password required."
            res["type"] = "error"
        elif read_students(username, password):
            res["message"] = "Login sucessful! Welcome, {}.".format(username)
            res["type"] = "success"
        else:
            res["message"] = "Invalid username or password."
            res["type"] = "error"
    return render_template("login.html",data=res)

@app.route("/signup", methods=["POST", "GET"], strict_slashes=False)
def register():
    res = {}
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        username = request.form.get("username","").strip()
        fullname = request.form.get("fullname","").strip()
        password = request.form.get("password","").strip()
    
        if not all([username, email, password, fullname]):
            res["message"] = "All fields are required."
            res["type"] = "error"
        elif verification(email=email, username=username):
                res["message"] = " a student with that username or email already exists."
                res["type"] = "error"
        else:
            write_student(username, email, fullname, password)
            res["message"] = "Account creadte succesfullly! you can now login."
            res["type"] = "success"
    return render_template("signup.html", data=res)

@app.route("/forgotpassword", methods=["POST", "GET"], strict_slashes=False)
def forgot_password():
    res = {}
    if request.method == "POST":
        username= request.form.get("username", "").strip()
    
        if  not username:
            res["message"] = "Please enter your username."
            res["type"] = "error"
        elif get_student(username) is None:
            res["message"] = "No account found with that username."
            res["type"] = "error"
        else:
            return redirect(url_for("new_password", username=username))
    
    return render_template("password.html", data=res)



@app.route("/change_password", methods=["POST", "GET"], strict_slashes=False)
def new_password():
    
    res = {}
    username = request.args.get("username", "") or request.form.get("username", "")

    if not username:
        return redirect(url_for("forget"))


    if request.method == "POST":
        newpassword = request.form.get("newpassword", "").strip()
        confirmpassword = request.form.get("confirmpassword", "").strip()
        
        if not newpassword or not confirmpassword:
            res["message"] = "Both password fields are required."
            res["type"] = "error"
        elif newpassword != confirmpassword:
            res['message']= "Both password fields are required "
            res["type"] = "error"
        elif len(newpassword) < 6:
            res["message"] = "Password must be at least 6 characters."
            res["type"] = "error"
        else:
            update_password(username, newpassword)
            res["message"] = " Password updated sucessfully. you can now login."
            res["type"] = "success"
            return render_template("newpass.html", data=res, username=username)
    return render_template("newpass.html", data=res, username=username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)