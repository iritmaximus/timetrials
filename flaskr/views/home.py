from flask import render_template, redirect, url_for

from flaskr import app
from flaskr.utils.user import check_session


@app.route("/")
def navigate():
    if not check_session():
        return redirect(url_for("login"))
    return render_template("home.html")


@app.route("/api")
def api_help():
    return "This is the api route. You will end up here from clicking a course, game or cup part of any time."
