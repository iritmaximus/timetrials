from flask import Flask
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")

if getenv("POSTGRES_URL") and getenv("POSTGRES_URL").startswith("postgresql://"):
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("POSTGRES_URL")
else:
    postgres_host = getenv("POSTGRES_HOST")
    postgres_db = getenv("POSTGRES_DB")
    postgres_port = getenv("POSTGRES_PORT")
    postgres_user = getenv("POSTGRES_USER")
    postgres_password = getenv("POSTGRES_PASSWORD")
    postgres_variables = [postgres_host, postgres_db, postgres_port, postgres_user, postgres_password]

    for var in postgres_variables:
        if not var:
            raise ValueError("All environment variables not set")

    database_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url


# import flaskr.views
import flaskr.views.home
import flaskr.views.games
import flaskr.views.cups
import flaskr.views.courses
import flaskr.views.times
import flaskr.views.users
