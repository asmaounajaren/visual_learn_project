from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
def configure_db(app):
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = ""
    app.config["MYSQL_DB"] = "visual_learn_project"

    mysql = MySQL(app)
    return mysql