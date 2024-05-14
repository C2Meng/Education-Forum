from flask import Blueprint

question = Blueprint('question', __name__)

@question.route('/quiz')
def quiz():
    return "<p>quiz</p>"

@question.route('/result')
def result():
    return "<p>Result</p>"

@question.route('/create-quiz')
def create_quiz():
    return "<p>Create Quiz</p."

