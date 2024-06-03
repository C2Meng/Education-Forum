from flask import Blueprint, render_template
from flask_login import current_user

teacher = Blueprint('teacher', __name__)
question = Blueprint('question', __name__)


@teacher.route('/discovery')
def discovery():
    return render_template('discovery.html', user=current_user)

@teacher.route('/admin_home')
def admin():
<<<<<<< HEAD
    return render_template('admin_home.html', user=current_user)

@question.route('/quiz')
def display_quiz():
    return render_template('quiz.html', user=current_user)
=======
    return render_template('admin_home.html')

@teacher.route('/quiz_data')
def quiz_data():
    return render_template('quiz_data.html')
>>>>>>> main
