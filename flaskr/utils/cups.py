from flaskr.database import db


def query_cups():
    sql = "SELECT name, id FROM cups"
    result = db.session.execute(sql).fetchall()
    return result


def get_cup_name(id: int):
    sql = "SELECT name FROM cups WHERE id=:id"
    result = db.session.execute(sql, {"id": id}).fetchone()
    if result:
        return result[0]
    else:
        raise ValueError("No cup with id found")


def get_cup_id(course_id: int):
    sql = "SELECT cups_id FROM courses WHERE id=:course_id"
    result = db.session.execute(sql, {"course_id": course_id}).fetchall()
    if result:
        return result[0]
    else:
        raise ValueError("No cup found for current course")


def get_all_times_in_cup(id: int) -> list[str]:
    """Queries the database for all times made in the wanted cup"""

    sql = """
    SELECT courses.name, games.name, times.timems, users.username
    FROM times
        JOIN courses ON times.course_id=courses.id
        JOIN games ON times.game_id=games.id
        JOIN users ON times.user_id=users.id
    WHERE times.cup_id=:id
    """

    result = db.session.execute(sql, {"id": id}).fetchall()
    return result
