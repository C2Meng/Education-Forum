#database models for users, and notes
from . import db #dot means everything
from flask_login import UserMixin #custom class
from sqlalchemy.sql import func #automate time data collection to store 

class Note(db.Model):
    id = db.Column(db.Integer, primary_key= True) #unique key with UNIQUE value to identify each record in a table
    data =db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #get current date time with default
    #foreign key relationships for note-user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #user id references User class and the id under it

#look up one to many , and many to one relationships



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    email = db.Column(db.String(150), unique=True) #unique to prevent duplicate email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #here will be capital N, because of course its supposed to be that way

