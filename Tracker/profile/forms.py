from Tracker.helpers import CheckProfanity
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from werkzeug.security import check_password_hash
from flask_login import current_user
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, HiddenField, TelField
from Tracker.models import User
from wtforms.validators import InputRequired, Length, ValidationError

class profileForm(FlaskForm):
    submit = SubmitField('UPDATE', id="save-button")
    
    banner = TextAreaField(u"Write here what you're open to collaborate with",id="motto", validators=[InputRequired(),Length(min=20, max=200), CheckProfanity()])
    
    profilePicture = FileField('Update Profile Picture', validators=[FileAllowed(['jpeg', 'png', 'jpg', 'webp'])])
    
    username = StringField(id='username', validators=[InputRequired(), Length(max=50), CheckProfanity()])
    
    def validate_username(self, username):
        if User.query.filter_by(username=username.data) == True:
            raise ValidationError("Username already taken")
    
    first_name = StringField('First Name', id="first-name", validators=[InputRequired(message="Please add your username"), Length(max=50), CheckProfanity()])
    
    last_name = StringField('Last Name', id="last-name", validators=[InputRequired(message="Please add your last name"), Length(max=50), CheckProfanity()])
    
    address = StringField(u'Address', id="address", validators=[Length(max=300), CheckProfanity()]) 
    
    country = HiddenField(id="country-input", validators=[InputRequired("Please add your country"), CheckProfanity()])
    
    skills = StringField('Skills', id="skills", validators=[Length(max=200, message="150 character limit"),CheckProfanity()])
    
    phone = TelField(validators=[Length(max=15, message="Accepts 15 numbers only")])
    
class ChangePassword(FlaskForm):
    password = PasswordField(id="old-password-input",validators=[InputRequired("Please input old password")])
    
    def validate_password(self, password):
        user = User.query.filter_by(email=current_user.email)

        if check_password_hash(user, password.data) == False:
            raise ValidationError("Password does not match database records")
        
    newPassword = PasswordField('Enter new Password', id="new-password-input", validators=[InputRequired("PLease input new password")])
    
    update = SubmitField(u'UPDATE', id="new-password-update-button")