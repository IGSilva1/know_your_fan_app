from flask import Flask
from .routes.main import main
from .extensions import db, login_manager  # <-- import correto

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(main)
    return app

from .extensions import db, login_manager
from .user import User  # <-- import seu modelo

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
