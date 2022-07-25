from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length 
from Tracker.helpers import CheckProfanity
from wtforms.validators import ValidationError
from Tracker.models import User

class RegisterForm(FlaskForm):
    register_username = StringField(u'Username', id="username", validators=[InputRequired(message="Add A Username"), Length(min=2,max=50), CheckProfanity(), Length(min=2,max=50)])

    def validate_register_username(self, register_username):
        
        if not register_username.data:
            raise ValidationError("Username cannot be empty")
        
        user = User.query.filter_by(username=register_username.data).first()

        if user:
            raise ValidationError("Username already taken") 
   
    # <input type="text" id="username" class="username" required name="username" placeholder="Username" minlength="2" maxlength="30">
 
    register_email = EmailField(u'Email', id="register-email", validators=[InputRequired(message="Should be a working email"), CheckProfanity(), Length(min=2,max=120)])
    
    def validate_register_email(self, register_email):
        
        if not register_email.data:
            raise ValidationError("Email cannot be empty")        
        
        if "@" not in register_email.data and ".com" not in register_email.data:
            raise ValidationError("Not an email")
        
        user = User.query.filter_by(email=register_email).first()

        if user:
            raise ValidationError("Email already taken")
            
    # <input type="email" id="email" class="email" required name="email" placeholder="Email">

    register_password = PasswordField(u'Password', id="regpassword", validators=[InputRequired("Please add a password"), CheckProfanity(), Length(min=2, max=40)])

    def validate_register_password(self, register_password):
        if not register_password.data:
            raise ValidationError("Password cannot be empty")
        
    # <input type="password" id="regpassword" required name="password" placeholder="Password" minlength="1" maxlength="40">
    
class LoginForm(FlaskForm):
    login_email = EmailField(u'Email', id="login-email", validators=[InputRequired(message="Should be a working email"), CheckProfanity(), Length(min=2,max=120)])
    
    def validate_login_email(self, login_email):
        
        if "@" not in login_email.data and ".com" not in login_email.data:
            raise ValidationError("Not an email")
        
        if not login_email.data:
            raise ValidationError("Email cannot be empty")
        
        user = User.query.filter_by(email=login_email).first()

        if not user:
            raise ValidationError("Email not found or User not yet registered")
    
    # <input type="email" class="email" name="email" placeholder="Email">

    login_password = PasswordField(u'Password', id="logpassword", validators=[InputRequired("Please add a password"), CheckProfanity(), Length(min=2, max=40)])

    def validate_login_password(self, login_password):
        if not login_password.data:
            raise ValidationError("Password cannot be empty")
        
    # <input type="password" id="regpassword" required name="password" placeholder="Password" minlength="1" maxlength="40">