from flaskr.database import db


def query_games():
    sql = "SELECT name FROM games"
    result = db.session.execute(sql).fetchall()
    print(result)
    return result
