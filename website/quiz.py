from flask import Blueprint


quiz = Blueprint('quiz',__name__)

@quiz.route('/quiz')
def quiz():
    return "<p>Quiz</p>"


@quiz.route('/quiz_submit')
def quiz_submit():
    return "<p>quiz_submit</p>"