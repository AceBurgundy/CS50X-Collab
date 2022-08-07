from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length 
from Tracker.helpers import CheckProfanity
from wtforms.validators import ValidationError
from Tracker.models import User

class RegisterForm(FlaskForm):
    register_username = StringField(u'Username', id="username", validators=[DataRequired(message="Add A Username"), Length(min=2,max=50), CheckProfanity(), Length(min=2,max=50)])

    def validate_register_username(self, register_username):
        
        if not register_username.data:
            raise ValidationError("Username cannot be empty")
        
        user = User.query.filter_by(username=register_username.data).first()

        if user:
            raise ValidationError("Username already taken") 
    
    register_email = EmailField(u'Email', id="register-email", validators=[DataRequired(message="Should be a working email"), CheckProfanity(), Length(min=2,max=120)])
    
    def validate_register_email(self, register_email):
        
        if not register_email.data:
            raise ValidationError("Email cannot be empty")        
        
        if "@" not in register_email.data and ".com" not in register_email.data:
            raise ValidationError("Not an email")
            
        user = User.query.filter_by(email=register_email.data).first()

        if user:
            raise ValidationError("Email already taken")
            
    register_password = PasswordField(u'Password', id="regpassword", validators=[DataRequired("Please add a password"), CheckProfanity(), Length(min=2, max=40)])

    def validate_register_password(self, register_password):
        if not register_password.data:
            raise ValidationError("Password cannot be empty")    
class LoginForm(FlaskForm):
    login_email = EmailField(u'Email', id="login-email", validators=[DataRequired(message="Should be a working email"), CheckProfanity(), Length(min=2,max=120)])
    
    def validate_login_email(self, login_email):
        
        if "@" not in login_email.data and ".com" not in login_email.data:
            raise ValidationError("Not an email")
        
        if not login_email.data:
            raise ValidationError("Email cannot be empty")
        
        user = User.query.filter_by(email=login_email.data).first()

        if not user:
            raise ValidationError("Email not found or User not yet registered")
    
    login_password = PasswordField(u'Password', id="logpassword", validators=[DataRequired("Please add a password"), CheckProfanity(), Length(min=2, max=40)])

    def validate_login_password(self, login_password):
        if not login_password.data:
            raise ValidationError("Password cannot be empty")