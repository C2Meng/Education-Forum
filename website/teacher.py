from flask import Blueprint, render_template
from website import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Quiz, Question, Answer


teacher = Blueprint('teacher', __name__)

@teacher.route('/discovery')
def discovery():
    return render_template('discovery.html')


@teacher.route('/quiz_data')
def quiz_data():
    return render_template('quiz_data.html')

