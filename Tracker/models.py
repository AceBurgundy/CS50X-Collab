from datetime import datetime
from Tracker import db, login_manager
from flask_login import UserMixin

"""
The function below is a callback used to reload the user object from the user ID stored in the session. 
It should take the str ID of a user, and return the corresponding user object. For example:
"""


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Project Collaborators


collaborators = db.Table("project_collaborators",
                         db.Column('id', db.Integer, primary_key=True),
                         db.Column('user_id', db.Integer, db.ForeignKey(
                             'user.id'), nullable=False),
                         db.Column('project_id', db.Integer, db.ForeignKey(
                             'project.id'), nullable=False),
                         db.Column('joined_datetime', db.DateTime,
                                   nullable=False, default=datetime.now),
                         db.Column('left_datetime', db.DateTime)
                         )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    skills = db.Column(db.String(200))
    banner = db.Column(db.String(200))
    email = db.Column(db.String(120), unique=True, nullable=False)
    country = db.Column(db.String(60))
    address = db.Column(db.String(300))
    phone = db.Column(db.String(15))
    profile_picture = db.Column(
        db.String(100), nullable=False, default='default.jpg')
    password = db.Column(db.String(200), nullable=False)
    creation_date = db.Column(db.DateTime(), default=datetime.now)
    last_online = db.Column(
        db.DateTime(), default=datetime.now, onupdate=datetime.now)

    # this is not a column so we wont see a projects column in the User database. Instead,
    # it runs a additional querry in the backrground to match the projects that the user has created

    project = db.relationship('Project', backref='author', lazy=True)

    comment = db.relationship('TicketComment', backref='sender', lazy=True)

    replies = db.relationship('TicketCommentReplies',
                              backref='sender', lazy=True)

    collaborated_projects = db.relationship(
        'Project', secondary=collaborators, backref='collaborators')

    def __repr__(self):
        return f"User('{self.username}') "


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(10), nullable=False, default="Queue")
    creation_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    description = db.Column(db.String(200), nullable=False)
    deadline = db.Column(db.Date, nullable=False)
    bookmark_state = db.Column(db.Boolean, nullable=False, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    tickets = db.relationship('Ticket', backref='this_project', lazy=True)

    messages = db.relationship(
        'Conversations', backref='this_project', lazy=True)

    def __repr__(self):
        return f"Project('{self.title}','{self.status}','{self.creation_date}','{self.description}','{self.deadline}','{self.bookmark_state}')"


class Conversations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(60), nullable=False)
    message = db.Column(db.Text)
    deletion_date = db.Column(db.DateTime)
    sent_date = db.Column(db.DateTime, nullable=False,
                          default=datetime.now, onupdate=datetime.now)

    project_id = db.Column(db.Integer, db.ForeignKey(
        'project.id'), nullable=False)

    def __repr__(self):
        return f"Conversations('{self.sender}','{self.message}')"


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(10), nullable=False, default='Pending')
    creation_date = db.Column(db.DateTime(), default=datetime.now)
    assigned_user = db.Column(db.String(50), nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    priority = db.Column(db.String(6), nullable=False, default='Low')
    deadline = db.Column(db.Date, nullable=False)
    bookmark_state = db.Column(db.Boolean, nullable=False, default=False)

    project_id = db.Column(db.Integer, db.ForeignKey(
        'project.id'), nullable=False)

    comments = db.relationship(
        'TicketComment', backref='this_ticket', lazy=True)

    def __repr__(self):
        return f"Ticket('{self.name}','{self.content}','{self.status}','{self.assigned_user}','{self.priority}','{self.created_by}','{self.deadline}','{self.bookmark_state}')"


class TicketComment(db.Model):
    __tablename__ = 'ticket_comment'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    sent_date = db.Column(db.DateTime, nullable=False,
                          default=datetime.now, onupdate=datetime.now)
    liked_state = db.Column(db.Boolean, nullable=False, default=False)

    likes = db.relationship(
        'TicketCommentLikes', backref='originated_comment', lazy=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    ticket_id = db.Column(db.Integer, db.ForeignKey(
        'ticket.id'), nullable=False)

    replies = db.relationship(
        'TicketCommentReplies', backref='originated_comment', lazy=True)

    def __repr__(self):
        return f"TicketComment('{self.comment}','{self.liked_state}','{self.replies}')"


class TicketCommentReplies(db.Model):
    __tablename__ = 'ticket_comment_replies'
    id = db.Column(db.Integer, primary_key=True)
    reply = db.Column(db.Text)
    deletion_date = db.Column(db.DateTime)
    sent_date = db.Column(db.DateTime, nullable=False,
                          default=datetime.now, onupdate=datetime.now)
    liked_state = db.Column(db.Boolean, nullable=False, default=False)

    likes = db.relationship(
        'TicketCommentLikes', backref='originated_reply', lazy=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    ticket_comment_id = db.Column(db.Integer, db.ForeignKey(
        'ticket_comment.id'), nullable=False)

    def __repr__(self):
        return f"Replies('{self.reply}','{self.ticket_comment_id}','{self.liked_state}')"


class TicketCommentLikes(db.Model):
    __tablename__ = 'ticket_comment_likes'
    id = db.Column(db.Integer, primary_key=True)

    ticket_comment_id = db.Column(db.Integer, db.ForeignKey(
        'ticket_comment.id'))

    ticket_replies_id = db.Column(db.Integer, db.ForeignKey(
        'ticket_comment_replies.id'))

    def __repr__(self):
        return f"Likes('{self.id}','{self.ticket_comment_id}','{self.ticket_replies_id}')"
