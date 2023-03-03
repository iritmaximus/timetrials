from flask import render_template, redirect, url_for, request, session

from flaskr import app
from flaskr.utils.times import query_times, add_time


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
