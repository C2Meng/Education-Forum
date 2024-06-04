from flask import Blueprint, render_template
<<<<<<< HEAD
from flask_login import current_user
=======
from website import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Quiz, Question, Answer

>>>>>>> c41f1a04c4df02117703690154029e7818a01ad6

teacher = Blueprint('teacher', __name__)

@teacher.route('/discovery')
def discovery():
    return render_template('discovery.html', user=current_user)

<<<<<<< HEAD
@teacher.route('/admin_home')
def admin():
   return render_template('admin_home.html', user=current_user)

=======
>>>>>>> c41f1a04c4df02117703690154029e7818a01ad6

@teacher.route('/quiz_data')
def quiz_data():
    return render_template('quiz_data.html')

