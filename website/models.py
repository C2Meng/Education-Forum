from website import db
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import func #implements automatic time recording




















class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key= True)  #creating unique id for quiz 
    title = db.Column(db.String(100), nullable=False) #nullable=false means not accepting null values
    description = db.Column(db.String(200)) #actually instructions for the quiz, should appear before student answers quiz
    subject = db.Column(db.String(100), nullable= False)
    questions = db.relationship('Question', backref ='quiz', lazy=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable = False)
    text = db.Column(db.String(150), nullable = False)
    answers = db.relationship('Answer', backref='question', lazy = True)

class Answer(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    text = db.Column(String(100), nullable=False)
    is_correct =db.Column(db.Boolean, nullable = False)


#this should be keep track of student history based on past quiz results
#shown history should include: what quiz, what subject, score, date, (and potentially mistakes student made)
#class Result(db.Model):
#user=
#score=
#date_answered=

    

