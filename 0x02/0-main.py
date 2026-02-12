#!/usr/bin/python
"""entry point for flask app"""
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    return "Hello World"


@app.route("/hello/<name>", methods=["GET"], strict_slashes=False)
def hello(name):
    return f"Hello{name}"


if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=5000, debug=True)