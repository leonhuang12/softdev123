from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.models import init_db
from config import Config

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    init_db()

    return app