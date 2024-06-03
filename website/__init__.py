from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello kitty'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' #this made the whole thing work
    db.init_app(app) # init connection to db

    from .views import views
    from .auth import auth
    from .question import question
    from .teacher import teacher
    


    
   

    from .models import Quiz, Question, Answer
    with app.app_context():
        db.create_all()

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(question, url_prefix='/')
    app.register_blueprint(teacher, url_prefix='/')
   
    
    return app 

