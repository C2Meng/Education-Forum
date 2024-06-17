from flask import Blueprint, render_template
from flask_login import current_user
from website import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Quiz, Question, Answer, StudentResult
from sqlalchemy import func


teacher = Blueprint('teacher', __name__)

@teacher.route('/discovery', methods = ['GET','POST'])
def discovery():
    quizzes = Quiz.query.all()
    return render_template('discovery.html', quizzes=quizzes, user=current_user)

@teacher.route('/admin_home',methods = ['GET'] )
def admin_home():
    quizzes = Quiz.query.all()
    return render_template('admin_home.html', quizzes=quizzes, user=current_user)

@teacher.route('/quiz_data/<int:quiz_id>', methods = ['GET','POST'])
def quiz_data(quiz_id):
    quiz = Quiz.query.get(quiz_id)

    # Subquery to get the minimum id for each user in each quiz
    subquery = db.session.query(
        func.min(StudentResult.id).label('min_id')
    ).filter(
        StudentResult.quiz_id==quiz_id
    ).group_by(StudentResult.user_id).subquery()
    
    # Query to get the first entry for each user (display first attempt score only)
    first_results = db.session.query(StudentResult).filter(
        StudentResult.id == subquery.c.min_id
    ).all()
    
    return render_template('quiz_data.html', user=current_user, quiz=quiz, all_results=first_results)