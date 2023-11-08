from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

# Flask Form: Login
class LoginForm(FlaskForm):
    username = StringField(label= 'Username' , validators=[Email(), DataRequired()])
    password = PasswordField(label= 'Password' , validators=[Length(min=5), DataRequired()])
    submit = SubmitField(label= 'Sign In')


