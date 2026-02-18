#!/usr/bin/python
"""an entry point to flask app"""
from flask import Flask, render_template, request
from utl import read_student, write_student

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    return "Hello World"

@app.route("/login", methods=[ "POST", "GET"], strict_slashes=False)
def login():
    return render_template("login.html")

@app.route("/signup", methods={"POST", "GET"}, strict_slashes=False)
def register():
    data = request.get_data()
    res= {}
    if read_student(data):
        res["message"] = "student already exists"
    else:
        write_student(data)
        res["message"] = "student created sucessfully"
    return render_template("signup.html", **res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)