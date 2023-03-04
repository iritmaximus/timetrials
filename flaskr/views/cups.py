from flask import render_template, redirect
from flaskr import app
from flaskr.utils.cups import (
    query_cups,
    get_cup_name,
    get_all_times_in_cup,
    query_cup_by_name,
)


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
    except ValueError as e:
        return render_template("error.html", message=f"Incorrect id, {e}")
    times = get_all_times_in_cup(cup_id)
    print(times)
    if times:
        return render_template(
            "cup_id.html", cup_name=cup_name, times=times, times_exist=True
        )
    else:
        return render_template("cup_id.html", times_exist=False)


@app.route("/api/cup/<string:cup_name>")
def get_cup_by_name(cup_name: str):
    try:
        cup_name = str(cup_name).replace("%20", " ")
        cup_id = query_cup_by_name(cup_name)
        print(cup_id)
        return redirect(f"/cups/{cup_id}")
    except ValueError as e:
        return render_template("error.html", message=f"Error fetching the cup name {e}")
