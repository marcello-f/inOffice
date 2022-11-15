from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    trackers = db.relationship('Tracker')

class Tracker(db.Model, UserMixin):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    monday1 = db.Column(db.String)
    tuesday1 = db.Column(db.String)
    wednesday1 = db.Column(db.String)
    thursday1 = db.Column(db.String)
    friday1 = db.Column(db.String)
    monday2 = db.Column(db.String)
    tuesday2 = db.Column(db.String)
    wednesday2 = db.Column(db.String)
    thursday2 = db.Column(db.String)
    friday2 = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))