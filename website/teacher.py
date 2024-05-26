from flask import Blueprint, render_template

teacher = Blueprint('teacher', __name__)

@teacher.route('/discovery')
def discovery():
    return render_template('discovery.html')