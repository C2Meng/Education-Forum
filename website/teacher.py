from flask import Blueprint, render_template
from flask_login import current_user
from website import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Quiz, Question, Answer


teacher = Blueprint('teacher', __name__)

@teacher.route('/discovery')
def discovery():
    return render_template('discovery.html', user=current_user)

@teacher.route('/admin_home',methods = ['GET'] )
def admin_home():
    quizzes = Quiz.query.all()
    return render_template('admin_home.html', quizzes=quizzes, user=current_user)

@teacher.route('/quiz_data/<int:quiz_id>', methods = ['GET','POST'])
def quiz_data(quiz_id):
    quiz = Quiz.query.get(quiz_id)
    return render_template('quiz_data.html', user=current_user, quiz=quiz)