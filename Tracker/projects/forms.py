from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import InputRequired, Length 
from Tracker.helpers import CheckProfanity


class newProject(FlaskForm):
    title = StringField(u'title', id="add-project-input", validators=[InputRequired(message="Your project needs a title"), Length(min=5,max=50), CheckProfanity(), Length(max=50)])
    
    description = TextAreaField(u'Description', id="add-project-description",validators=[InputRequired(message="Your project needs a description"), CheckProfanity(), Length(min=5,max=200)])
    
    deadline = DateField(validators=[InputRequired()]) 
        
    add = SubmitField(u'ADD', id="add-project-deadline")