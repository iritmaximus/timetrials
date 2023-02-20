from flask import render_template, request, redirect, url_for

from flaskr import app
from flaskr.database import test_db, create_db, reset_db
from flaskr.user import (
    check_user_login,
    generate_session,
    check_session,
    create_new_user,
)


@app.route("/")
def navigate():
    if not check_session():
        return redirect(url_for("login"))
    return render_template("home.html")


# TODO show 3 games with most times submitted
@app.route("/games")
def get_games():
    return "List of games"


# TODO show 3 courses with most activity
@app.route("/courses")
def get_courses():
    return "List of courses"


# TODO show 3 newest times submitted
@app.route("/times")
def get_times():
    return "List of times"


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
        if check_user_login(username, password):
            generate_session(username)
            return redirect(url_for("navigate"))

        else:
            print("*** incorrect login ***")
            return redirect(url_for("login"))

    else:
        return "Incorrect http method"


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


@app.route("/db/init")
def initialize_db():
    return create_db()


@app.route("/db/reset")
def reset_database():
    reset_db()
    return "Initialization successful"


@app.route("/db")
def test_db_route():
    return test_db()
