
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
# from tempfile import mkdtemp

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config['SECRET_KEY'] = 'Adrian2001.'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collab.db'
db = SQLAlchemy(app)



"""
The login manager contains the code that lets your application and Flask-Login work together, 
such as how to load a user from an ID, where to send users when they need to log in, and the like.
"""

login_manager = LoginManager(app)
login_manager.login_view = 'user.login'

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

from Tracker.user.views import user
from Tracker.profile.views import profile
from Tracker.projects.views import projects
from Tracker.index.views import index

app.register_blueprint(user)
app.register_blueprint(profile)
app.register_blueprint(projects)
app.register_blueprint(index)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
