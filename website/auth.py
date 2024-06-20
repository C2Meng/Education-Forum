from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError



auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user_status = request.form.get('user_status') 

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password. Please try again', category='error')
        else:
            flash('User not found. Please sign up.', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        full_name = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user_status = request.form.get('user_status').strip() 

        user = User.query.filter_by(email=email).first()

        # Validate form inputs
        if user:
            flash('Email already exists. Please sign up with another email.', category ='error')
        if len(email) < 5 or '@' not in email or '.com' not in email:
            flash('Please enter a valid email', category='error')
        elif len(full_name) < 2:
            flash('Please enter your full name.', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters.', category='error')
        elif password1 != password2:
            flash('Please confirm password again.', category='error')
        elif user_status not in ["Teacher", "Student"]:
            flash('Please select a valid role.', category='error')
        
        else:
                new_user = User(email=email, full_name=full_name, password=generate_password_hash(password1), user_status=user_status)

                # Create new User object and add to session
                try:
                    db.session.add(new_user)
                    db.session.commit()
                    login_user(new_user, remember=True)
                    flash('Account created!', category='success')
                    return redirect(url_for('views.home'))
                except IntegrityError:
                    db.session.rollback()
                  

    return render_template("sign_up.html", user=current_user)

    full_name = request.form.get('fullName','')
    password1 = request.form.get('password1','') #redundant codes to store the info user keyed in, values keyed in html form
    email = request.form.get('email', '')
    password2 = request.form.get('password2','')
    user_status = request.form.get('user_status')
    return render_template("sign_up.html", user=current_user, full_name=full_name, 
                           password1=password1, email=email, password2=password2, user_status=user_status)
