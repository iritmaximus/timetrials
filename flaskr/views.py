from flask import render_template, request, redirect, url_for, session

from flaskr import app
from flaskr.database import test_db, create_db, reset_db
from flaskr.user import (
    user_login,
    generate_session,
    check_session,
    create_new_user,
)
from flaskr.times import query_times, add_time
from flaskr.games import query_games
from flaskr.cups import query_cups
from flaskr.courses import query_courses


@app.route("/")
def navigate():
    if not check_session():
        return redirect(url_for("login"))
    return render_template("home.html")


@app.route("/games")
def get_games():
    games = query_games()
    if games is None:
        return render_template("games.html", games_exist=False)
    return render_template("games.html", games=games, games_exist=True)


@app.route("/cups")
def get_cups():
    cups = query_cups()
    if cups is None:
        return render_template("cups.html", cups_exist=False)
    return render_template("cups.html", cups=cups, cups_exist=True)


@app.route("/courses")
def get_courses():
    courses = query_courses()
    if courses:
        return render_template("courses.html", courses=courses, courses_exist=True)
    return render_template("courses.html", courses_exist=False)


@app.route("/times")
def get_times():
    times = query_times()
    print(times)
    if times is not None:
        return render_template("times.html", times=times, times_exist=True)
    return render_template("times.html", times_exist=False)


@app.route("/create/time", methods=["GET", "POST"])
def create_time():
    if request.method == "GET":
        return render_template("addtime.html")
    elif request.method == "POST":
        if session.get("name") is None:
            return redirect(url_for("login"))
        game = request.form["game"]
        course = request.form["course"]
        time = request.form["time"]
        user = session["name"]
        add_time(game, course, time, user)
        return redirect(url_for("get_times"))
    else:
        return "Error: Incorrect method"


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


# TODO remove these when ready
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
