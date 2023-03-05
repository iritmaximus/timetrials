from flaskr.database import db


def query_cups():
    sql = "SELECT name, id FROM cups"
    result = db.session.execute(sql).fetchall()
    sql = "SELECT count(cups.id) FROM cups"
    count = db.session.execute(sql).fetchone()
    db.session.close()
    return result, count[0]


def query_cup_by_name(cup_name: str):
    sql = """
    SELECT cups.id FROM cups WHERE cups.name=:cup_name
    """
    result = db.session.execute(sql, {"cup_name": cup_name}).fetchone()
    db.session.close()
    if result:
        return result[0]
    else:
        raise ValueError(f"No cup with name {cup_name} found")


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
    db.session.close()
    if result:
        return result[0]
    else:
        raise ValueError("No cup found for current course")


def get_all_times_in_cup(id: int):
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
    sql = "SELECT count(times.id) FROM times WHERE times.cup_id=:id"
    count = db.session.execute(sql, {"id": id}).fetchone()
    db.session.close()
    return result, count[0]
