from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

# Flask Form: Register
class RegisterForm(FlaskForm) :
    firstname = StringField(label= 'First Name' , validators=[Length(min=2 ,max=60), DataRequired()])
    lastname = StringField(label= 'Last Name' , validators=[Length(min=2 ,max=60), DataRequired()])
    email = StringField(label= 'Email' , validators=[Email(), DataRequired()])
    phone = StringField(label= 'Phone Number' , validators=[Length(min=10 ,max=12), DataRequired()])
    address = StringField(label= 'Address' , validators=[Length(max=120), DataRequired()])
    submit = SubmitField(label= 'Submit')



