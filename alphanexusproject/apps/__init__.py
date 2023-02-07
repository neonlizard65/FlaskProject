from flask import Flask, request, Blueprint
from apps.api import api
from flaskext.mysql import MySQL
from extensions import mysql


def create_app():
    app = Flask(__name__)
    app.config["MYSQL_DATABASE_USER"] = 'aleksei'
    app.config["MYSQL_DATABASE_PASSWORD"] = '**********'
    app.config["MYSQL_DATABASE_DB"] = 'alphanexus'
    app.config["MYSQL_DATABASE_HOST"] = 'localhost'
    app.config["MYSQL_DATABASE_PORT"] = 3306
    mysql.init_app(app)
    
    app.register_blueprint(api, url_prefix="/api/")
    
    return app
