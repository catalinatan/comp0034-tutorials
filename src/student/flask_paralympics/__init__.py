import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


# Create a SQLAlchemy declarative base object called Base to be used in the models (Python classes)
class Base(DeclarativeBase):
    pass


# Create a SQLAlchemy object called db, the Base object is passed to the SQLAlchemy object
db = SQLAlchemy(model_class=Base)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # Set the location of the database file in the app's instance folder
        SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(app.instance_path, 'paralympics.db'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialise the database
    # Make sure you already defined SQLALCHEMY_DATABASE_URI in the app.config
    db.init_app(app)

    return app