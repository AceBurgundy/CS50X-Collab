from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from Tracker.config import Config

login_manager = LoginManager()
login_manager.login_view = 'user.login'

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    login_manager.init_app(app)
    db.init_app(app)
    
    from Tracker.user.views import user
    from Tracker.profile.views import profile
    from Tracker.projects.views import projects
    from Tracker.index.views import index
    from Tracker.errors.handlers import errors

    app.register_blueprint(user)
    app.register_blueprint(profile)
    app.register_blueprint(projects)
    app.register_blueprint(index)
    app.register_blueprint(errors)

    @app.after_request
    
    def after_request(response):
        """Ensure responses aren't cached"""
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response
    return app