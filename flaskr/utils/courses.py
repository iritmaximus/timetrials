from flaskr.database import db


def query_courses():
    sql = "SELECT courses.name, games.name, cups.name FROM courses JOIN games ON games.id=courses.game_id JOIN cups ON cups.id=courses.cup_id"
    result = db.session.execute(sql).fetchall()
    return result


def query_course_by_name(course_name: str):
    sql = """
    SELECT games.name, cups.name, times.timems, users.username
    FROM times
        JOIN games ON games.id=times.game_id
        JOIN cups ON cups.id=times.cup_id
        JOIN users ON users.id=times.user_id
    WHERE times.course_id in (SELECT id FROM courses WHERE name=:course_name)
    """
    result = db.session.execute(sql, {"course_name": course_name}).fetchall()
    return result
