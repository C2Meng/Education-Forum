from flask import Flask, current_app as app
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user

db = SQLAlchemy()
DB_NAME = "app.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello kitty'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' #this made the whole thing work
    db.init_app(app)  # Initialize connection to the database

    # Import blueprints and models
    from .views import views
    from .auth import auth
    from .question import question
    from .teacher import teacher
    from .student import student

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(question, url_prefix='/')
    app.register_blueprint(teacher, url_prefix='/')
    app.register_blueprint(student, url_prefix='/')

    from .models import User  # Import models

    # Create database if it doesn't exist
    with app.app_context():
        create_database(app)

    # Setup Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

        if current_user.is_authenticated:
            user_status = User_status.query.filter_by(id=current_user.user_status_id).first()
            return dict(userStatus=user_status.status)
        return dict(userStatus=None)

    return app

def create_database(app):
    if not path.exists(f'website/{DB_NAME}'):
        with app.app_context():
            db.create_all()
            print('Created database!')
