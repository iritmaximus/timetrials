from flaskr.database import db


def query_cups():
    sql = "SELECT name FROM cups"
    result = db.session.execute(sql).fetchall()
    return result
