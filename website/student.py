from flask import Blueprint, render_template

student = Blueprint('student', __name__)

@student.route('/quizcode')
def quizcode():
    return render_template('quizcode.html')

@student.route('/score')
def score():
    return render_template('score.html')