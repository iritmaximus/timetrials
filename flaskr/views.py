from flask import render_template, request, redirect, url_for, flash

from flaskr import app
from flaskr.database import db, test_db, create_db
from flaskr.user import check_user_exists, generate_token


@app.route("/")
def navigate():
    sessionid = ""
    if not sessionid:
        redirect(url_for("login"))

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
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if check_user_exists(username, password):
            generate_token()
            return redirect(url_for("navigate"))
        else:
            flash("Incorrect login", "error")
            print("send notification: incorrect login")
            return redirect(url_for("login"))
    else:
        return "Incorrect http method"



        return f"Todo POST request {username} {password}"

@app.route("/createuser")
def createuser():
    return "new user created"

@app.route("/init")
def initialize_db():
    return create_db()


@app.route("/db")
def test_db_route():
    return test_db()
