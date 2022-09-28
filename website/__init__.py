from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']= "helloworld"
    app.static_folder = 'static'

    from .views import views
    app.register_blueprint(views, urlprefix="/")

    from .auth import auth
    app.register_blueprint(auth, urlprefix="/")

    return app