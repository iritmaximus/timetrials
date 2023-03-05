from flaskr.database import db


def query_games():
    sql = "SELECT name, id FROM games"
    result = db.session.execute(sql).fetchall()
    sql = "SELECT count(games.id) FROM games"
    count = db.session.execute(sql).fetchone()
    return result, count[0]


def query_game_by_name(game_name: str):
    sql = "SELECT id FROM games WHERE games.name=:game_name"
    result = db.session.execute(sql, {"game_name": game_name}).fetchone()
    if result:
        return result[0]
    else:
        raise ValueError(f"No game with name {game_name} found")


def get_game_name(id: int):
    sql = f"SELECT name FROM games WHERE id=:id"
    result = db.session.execute(sql, {"id": id}).fetchone()
    if result:
        return result[0]
    else:
        raise ValueError("No game with id found")


def get_all_times_in_game(id: int):
    sql = """
    SELECT courses.name, cups.name, times.timems, users.username
    FROM times
        JOIN courses ON courses.id=times.course_id
        JOIN cups ON cups.id=times.cup_id
        JOIN users ON users.id=times.user_id
    WHERE times.game_id=:id
    """
    results = db.session.execute(sql, {"id": id}).fetchall()
    sql = "SELECT count(times.id) FROM times WHERE times.game_id=:id"
    count = db.session.execute(sql, {"id": id}).fetchone()
    return results, count[0]
