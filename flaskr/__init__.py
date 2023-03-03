from flask import Flask
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")


# import flaskr.views
import flaskr.views.home
import flaskr.views.games
import flaskr.views.cups
import flaskr.views.courses
import flaskr.views.times
import flaskr.views.users
