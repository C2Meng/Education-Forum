#handles POST and GET requests

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User, User_status

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    user_status = User_status.query.filter_by(id=current_user.user_status_id).first()
    return render_template('home.html', user=current_user, userStatus=user_status.status)

