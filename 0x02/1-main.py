#!/usr/bin/python
"""an entry point to flask app"""
from flask import Flask, render_template, request, redirect, url_for, session
from utl import (read_students, write_student, verification, get_student, update_password,get_all_blogs,get_blog_by_id,create_blog,
                delete_blog, get_blogs_by_author)

app = Flask(__name__)
app.secret_key = "blogspace-secret-key-2026"


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    blogs = get_all_blogs()
    return render_template("index.html", blogs=blogs)


@app.route("/blog/<int:blog_id>", methods=["GET"], strict_slashes=False)
def view_blog(blog_id):
    blog = get_blog_by_id(blog_id)
    if blog is None:
        return redirect(url_for("index"))
    return render_template("blog.html", blog=blog)


@app.route("/dashboard", methods=["GET","POST"], strict_slashes=False)
def dashboard():
    if "username" not in session:
        return redirect(url_for(login))

    username = session["username"]
    res = {}

    if request.method == "POST":
        action = request.form.get("action", "")

        if action  == "create":
            title = request.form.get("title", "").strip()
            content = request.form.get("content", "").strip()
            if not title or not content:
                res["message"] = "Title and content are required"
                res["type"] = "error"
            else:
                create_blog(title, content, username)
                res["message"] = "Blog post published successfully"
                res["type"] = "success"

        elif action == "delete":
            blog_id = request.form.get("blog_id", "")
            if delete_blog(blog_id, username):
                res["message"] = "Post deleted"
                res["type"] = "success"
            else:
                res["message"] = "Could not delete that post."
                res["type"] = "error"

    my_blogs = get_blogs_by_author(username)
    return render_template("dashboard.html", data=res, blogs=my_blogs, username=username)

@app.route("/logout", methods=["GET"], strict_slashes=False)
def logout():
    session.clear()
    return redirect(url_for("index"))




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
            session["username"] = username
            return redirect(url_for("dashboard"))
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