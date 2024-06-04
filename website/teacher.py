from flask import Blueprint, render_template
from flask_login import current_user
from website import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Quiz, Question, Answer


teacher = Blueprint('teacher', __name__)

@teacher.route('/discovery')
def discovery():
    return render_template('discovery.html', user=current_user)

@teacher.route('/admin_home')
def admin():
   return render_template('admin_home.html', user=current_user)


@teacher.route('/quiz_data')
def quiz_data():
    return render_template('quiz_data.html', user= current_user)

