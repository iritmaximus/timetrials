# import bcrypt
from flask import session
from flaskr.database import db

from werkzeug.security import check_password_hash, generate_password_hash


def generate_session(name: str):
    print("session name", session.get("name"))
    session["name"] = name


def check_session() -> bool:
    if session.get("name") is not None and len(session["name"]) > 0:
        return True
    else:
        return False


def user_login(name: str, password: str) -> bool:
    # query sql
    # 1. check if username exists
    # 2. check if passwords match

    print("checking if username exists")
    sql = "SELECT password FROM users as u where u.username=:username"
    result = db.session.execute(sql, {"username": name}).fetchone()
    print("password:", result)
    if result is None:
        return False

    print("found username, checking password")
    if check_password_hash(result[0], password):
        print("password matches")
        return True

    return False


def check_username_exists(username: str) -> bool:
    sql = "SELECT COUNT(*) FROM users as u WHERE u.username=:username"
    result = db.session.execute(sql, {"username": username}).fetchone()
    print("result:", result)
    if result is not None:
        if result[0] == 0:
            return False
    return True


def create_new_user(name: str, text_password: str):
    # insert into sql
    # 1. username
    # 2. hashed password

    username = str(name)
    if check_username_exists(username):
        raise ValueError("Username exists")
    password = hash_password(text_password)

    print("inserting to db")
    sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
    db.session.execute(sql, {"username": username, "password": password})
    db.session.commit()
    print("success")


def hash_password(password: str) -> str:
    return generate_password_hash(password)
