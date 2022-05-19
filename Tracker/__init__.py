import os

from flask import Flask#, request, session
from flask_sqlalchemy import SQLAlchemy
#from flask_session import Session
from tempfile import mkdtemp
# from cs50 import SQL

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

# # Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///app.db")

from Tracker import routes

# # Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# @app.after_request
# def after_request(response):
#     """Ensure responses aren't cached"""
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Expires"] = 0
#     response.headers["Pragma"] = "no-cache"
#     return response
