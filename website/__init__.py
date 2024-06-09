from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager 

db = SQLAlchemy()
DB_NAME = "users.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello kitty'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' #this made the whole thing work
    db.init_app(app) # init connection to db

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
    
    from .models import Quiz, Question, Answer, User
    with app.app_context():
         create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app 

def create_database(app):
    if not path.exists('website/'+ DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')