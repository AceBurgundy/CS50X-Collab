from Tracker import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(200), nullable=False)

    #this is not a column so we wont see a projects column in the User database instead,
    #it runs a additional querry in the backrground to match the projects that the user has created
    project = db.relationship('Project', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}') "

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, unique=True, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Project('{self.title}','{self.date_posted}') "
