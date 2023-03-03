from flask import render_template

from flaskr import app
from flaskr.utils.courses import query_courses


@app.route("/courses")
def get_courses():
    courses = query_courses()
    if courses is None:
        return render_template("courses.html", courses_exist=False)
    return render_template("courses.html", courses=courses, courses_exist=True)


@app.route("/courses/<int:course_id>")
def get_course_by_id(course_id: int):
    try:
        course_id = int(course_id)
    except ValueError as e:
        return render_template("error.html", message=f"Incorrect id, {e}")
