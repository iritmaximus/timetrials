from flaskr.database import db

def query_courses():
    sql = "SELECT courses.name, games.name, cups.name FROM courses JOIN games ON games.id=courses.game_id JOIN cups ON cups.id=courses.cup_id"
    result = db.session.execute(sql).fetchall()
    return result
