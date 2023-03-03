from flask import render_template, request, redirect, url_for, session

from flaskr import app
from flaskr.database import test_db, create_db, reset_db
from flaskr.utils.user import check_session


@app.route("/")
def navigate():
    if not check_session():
        return redirect(url_for("login"))
    return render_template("home.html")


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
