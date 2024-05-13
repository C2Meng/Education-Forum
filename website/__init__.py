from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello kitty'

    from .views import views
    from .auth import auth
    from .quiz import quiz

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(quiz, url_prefix='/' )
    
    return app 