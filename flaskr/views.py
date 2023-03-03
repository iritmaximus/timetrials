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
from flaskr.games import query_games, get_game_name, get_all_times_in_game
from flaskr.cups import query_cups, get_cup_name, get_all_times_in_cup
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


@app.route("/games/<int:game_id>")
def get_game_by_id(game_id):
    try:
        game_id = int(game_id)
        game_name = get_game_name(game_id)
    except ValueError:
        return render_template(
            "error.html", message="Incorrect id, id not found or incorrect value"
        )
    times = get_all_times_in_game(game_id)
    return render_template("game_id.html", game_name=game_name, times=times)


@app.route("/cups")
def get_cups():
    cups = query_cups()
    if cups is None:
        return render_template("cups.html", cups_exist=False)
    return render_template("cups.html", cups=cups, cups_exist=True)


@app.route("/cups/<int:cup_id>")
def get_cup_by_id(cup_id):
    try:
        cup_id = int(cup_id)
        # TODO unnecessary sql query, name could be passed from the <a>
        cup_name = get_cup_name(cup_id)
    except ValueError:
        return render_template(
            "error.html", message="Incorrect id, id not found or incorrect value"
        )
    times = get_all_times_in_cup(cup_id)
    print(times)
    if times:
        return render_template(
            "cup_id.html", cup_name=cup_name, times=times, times_exist=True
        )
    else:
        return render_template("cup_id.html", times_exist=False)


@app.route("/courses")
def get_courses():
    courses = query_courses()
    if courses is None:
        return render_template("courses.html", courses_exist=False)
    return render_template("courses.html", courses=courses, courses_exist=True)


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
        try:
            add_time(game, course, time, user)
        except ValueError as e:
            print("Error adding the time", e)
            return redirect(url_for("create_time"))
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
