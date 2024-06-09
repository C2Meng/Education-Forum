from flask import Blueprint, render_template
from flask_login import current_user

student = Blueprint('student', __name__)

@student.route('/score')
def score():
    return render_template('score.html', user=current_user)