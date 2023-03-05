from flask import render_template

from flaskr import app
from flaskr.utils.courses import query_courses, query_course_by_name


@app.route("/courses")
def get_courses():
    courses, count = query_courses()
    if courses is None:
        return render_template("courses.html", courses_exist=False, count=count)
    return render_template(
        "courses.html", courses=courses, courses_exist=True, count=count
    )


@app.route("/courses/<int:course_id>")
def get_course_by_id(course_id: int):
    try:
        course_id = int(course_id)
    except ValueError as e:
        return render_template("error.html", message=f"Incorrect id, {e}")


@app.route("/api/course/<string:course_name>")
def get_course_by_name(course_name: str):
    try:
        course_name = str(course_name).replace("%20", " ")
        times = query_course_by_name(course_name)
        return render_template("course_name.html", course_name=course_name, times=times)
    except ValueError as e:
        return render_template("error.html", message=f"Failed to fetch course, {e}")
