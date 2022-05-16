from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .home import home as home_blueprint

from .config import Config

app = Flask(__name__)
app.secret_key = "skfafae12312da"
app.config.from_object(Config)

def create_app():
    app.register_blueprint(home_blueprint)
    
    return app