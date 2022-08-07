from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, AnyOf
from Tracker.helpers import CheckProfanity

class TicketForm(FlaskForm):
    name = StringField(u'title', id="form-title", validators=[DataRequired(), Length(max=50), CheckProfanity()])    
         
    description = TextAreaField(u'Description', id="form-description", validators=[DataRequired(), Length(max=200), CheckProfanity()])
    
    # comment = StringField(validators=[DataRequired(), CheckProfanity()])
    
    priority = SelectField(validators=[DataRequired(), CheckProfanity(), AnyOf(['Low', 'Medium', 'High'])], choices=[('Low','Low'),('Medium','Medium'), ('High','High')])
          
    status = StringField(default='pending', validators=[DataRequired(), Length(max=10)])
    
    deadline = DateField(validators=[DataRequired()]) 

    proceed = SubmitField(u'PROCEED', id="form-deadline")