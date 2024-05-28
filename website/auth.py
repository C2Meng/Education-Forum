from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        fullName = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user_status = request.form.get('user_status')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(fullName) < 2:
            flash('Full name must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('Password does not match.', category='error')
        elif len(password1) < 7:
            flash('Password must have at least 8 characters.', category='error')
        elif len(user_status) < 7:
            flash('User status must be more than 7 characters', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("sign_up.html")
