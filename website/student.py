from flask import Blueprint, render_template

student = Blueprint('student', __name__)

@student.route('/quizcode')
def discovery():
    return render_template('quizcode.html')

@student.route('/score')
def admin():
    return render_template('score.html')