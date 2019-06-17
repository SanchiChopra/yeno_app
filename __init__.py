"""Blog main module"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import MySQLdb

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

