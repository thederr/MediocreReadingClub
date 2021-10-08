# from datetime import timezone
# from enum import unique
# from . import db
# from flask_login import UserMixin
# from sqlalchemy.sql import func

# class Note(db.Model):
#     id= db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(100000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     ## One to many relationship ##
#     ## Storing a key on the child object that refs ##
#     ## the parent object. in this case note is child and user is parent ##
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150, unique=True)) #unique = true means no users can have the same email address
#     password = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))
#     notes = db.relationship('Note')

#______________________________________________________

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')