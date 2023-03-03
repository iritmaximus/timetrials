from flask import render_template, redirect, url_for, request, session
from flaskr import app

from flaskr.utils.user import (
    check_session,
    user_login,
    generate_session,
    create_new_user,
)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if check_session():
            # already logged in
            return redirect(url_for("navigate"))
        return render_template("login.html")

    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # TODO generate error messsage for incorrect login
        if user_login(username, password):
            generate_session(username)
            return redirect(url_for("navigate"))

        else:
            print("*** incorrect login ***")
            return redirect(url_for("login"))

    else:
        return "Incorrect http method"


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print("creating new user...")
        try:
            create_new_user(username, password)
        except ValueError as e:
            print("Error:", e)
            return redirect(url_for("signup"))

        return redirect(url_for("navigate"))

    else:
        print("incorrect method")
        return "Error: Incorrect method"
