from flask import Flask

from .config import Config

app = Flask(__name__)
app.secret_key = "skfafae12312da"
app.config.from_object(Config)

def create_app():
    return app
