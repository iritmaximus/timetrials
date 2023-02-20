from flaskr.database import db


def query_times():
    sql = "SELECT games.name, courses.name, times.timems, users.username FROM times JOIN games ON games.id=times.game_id JOIN courses ON courses.id=times.course_id JOIN users ON users.id=times.user_id"
    result = db.session.execute(sql).fetchall()
    print(result)
    return result


def add_time(game, course, time, user):
    sql = "SELECT id FROM games WHERE games.name=:game"
    game_id = db.session.execute(sql, {"game": game}).fetchone()
    if game_id is None:
        raise ValueError("No game_id found for", game)
    sql = "SELECT id FROM courses WHERE courses.name=:course"
    course_id = db.session.execute(sql, {"course": course}).fetchone()
    if course_id is None:
        raise ValueError("No course_id found for", course)
    sql = "SELECT id FROM users WHERE users.username=:user"
    user_id = db.session.execute(sql, {"user": user}).fetchone()
    if user_id is None:
        raise ValueError("No user_id found for", user)
    sql = "INSERT INTO times (game_id, course_id, timems, user_id) VALUES (:game_id, :course_id, :time, :user_id)"

    print(game_id, course_id, time, user_id)
    print(sql)

    db.session.execute(
        sql,
        {
            "game_id": game_id[0],
            "course_id": course_id[0],
            "time": time,
            "user_id": user_id[0],
        },
    )
    db.session.commit()
