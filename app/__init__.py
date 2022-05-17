from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .home import home as home_blueprint
from .login import login as login_blueprint


from .config import Config

# APP CONFIG
app = Flask(__name__)
app.secret_key = "skfafae12312da"
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# DB CONFIG
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(120))
    pass_hash = db.Column(db.String(128))

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    asset_name = db.Column(db.String(64))
    location = db.Column(db.String(120))
    updated = db.Column(db.String(128))

def create_app():
    app.register_blueprint(home_blueprint)
    app.register_blueprint(login_blueprint)

    
    return app