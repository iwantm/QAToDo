from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI_TODO')
app.config['SECRET_KEY'] = getenv('TODO_SECRET_KEY')

db = SQLAlchemy(app)
from application import routes, forms
