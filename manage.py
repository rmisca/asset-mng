from app import create_app

if __name__ == '__main__':
    create_app()

# from flask import Flask
# from flask import request

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello, world"

# @app.route("/greet")
# def greet():
#     return "Hello"

# @app.route("/greet/<name>")
# def greet_name(name):
#     return "Hello, " + name

# @app.route("/bye", methods = ['POST'])
# def bye():
#     return 'Draga ' + request.form["for"] + ' iti urez ' + request.form["wish"]