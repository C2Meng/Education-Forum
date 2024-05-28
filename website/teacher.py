from flask import Blueprint, render_template

teacher = Blueprint('teacher', __name__)

@teacher.route('/discovery')
def discovery():
    return render_template('discovery.html')

@teacher.route('/admin_home')
def admin():
    return render_template('admin_home.html')