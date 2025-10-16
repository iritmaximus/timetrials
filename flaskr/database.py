from os import getenv
from flaskr import app
from flask_sqlalchemy import SQLAlchemy
from random import randint


db = SQLAlchemy(app)

def create_db():
    print("Initializing the db...")
    db.session.execute(open("sql/schema.sql", "r").read())
    db.session.execute(open("sql/games.sql", "r").read())
    db.session.execute(open("sql/cups.sql", "r").read())
    db.session.execute(open("sql/courses.sql", "r").read())
    db.session.commit()
    db.session.close()
    print("Db initialization completed.")

    return "Success"


def reset_db():
    print("Resetting the db...")
    db.session.execute(open("sql/resettables.sql", "r").read())
    db.session.execute(open("sql/schema.sql", "r").read())

    db.session.execute(open("sql/games.sql", "r").read())
    db.session.execute(open("sql/cups.sql", "r").read())
    db.session.execute(open("sql/courses.sql", "r").read())
    db.session.commit()
    db.session.close()


def test_db():
    print("*********************** TESTING THE DB ***********************")

    sql = "DROP TABLE IF EXISTS test;"
    db.session.execute(sql)
    db.session.commit()

    sql = "CREATE TABLE IF NOT EXISTS test (id int primary key, greeting text);"
    db.session.execute(sql)
    db.session.commit()

    for x in range(10):
        sql = f"INSERT INTO test (id, greeting) VALUES ({randint(1,100)}, 'hello');"
        db.session.execute(sql)

    db.session.commit()

    result = db.session.execute("SELECT * FROM test;").fetchall()
    db.session.close()
    print(result)

    return "Working lol"
