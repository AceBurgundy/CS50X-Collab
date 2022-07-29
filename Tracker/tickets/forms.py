from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length
from Tracker.helpers import CheckProfanity

class newTicket(FlaskForm):
    name = StringField(InputRequired(), validators=[Length(max=50), CheckProfanity()])    
         
    description = StringField(InputRequired(), validators=[Length(max=200), CheckProfanity()])
        
    comment = StringField(InputRequired(), validators=[CheckProfanity()])
            
    status = StringField(InputRequired(), default='pending', validators=[Length(max=10)])