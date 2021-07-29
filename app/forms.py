from flask_wtf import Flaskform
from wtforms import StringField, PasswrodField, SumbitField
from wtforms.validators import Email, DataRequired 
#flask_wsp, what's wrong? 
sf

class LoginForm(FlaskForm): 
    email = StringField('Email Adderess', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

    #1:24:28