from sqlalchemy import text, Text
from app_files import db, app, login_manager
from flask_login import UserMixin
import json


with open("app_files/config.json") as c:
    params = json.load(c)["params"]

@login_manager.user_loader
def load_user(user):
    return Login.query.get(int(user))

app.app_context().push()


# Creating database

# Login Table
class Login(db.Model,UserMixin):
    '''
    id, username, password, designation
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(Text, nullable=False)
    password = db.Column(Text, nullable=False)
    designation = db.Column(Text, nullable=False)

# Register Table
class Register(db.Model):
    '''
    sno , firstname, lastname, gender, dob, email, ph_no, address
    '''
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(Text, nullable=False)
    lastname = db.Column(Text, nullable=False)
    gender = db.Column(Text, nullable=False)
    dob = db.Column(Text, nullable = False)
    email = db.Column(Text, nullable=False)
    ph_no = db.Column(Text, nullable=False)
    address = db.Column(Text, nullable=False)

db.create_all()


# If there is no 'admin' in the database, then create one 'admin' entry in the database, 
# Using the "Admin" details present in 'config.json' file.
# One can change the Admin Details from the 'config.json' file.
admin = Login.query.filter_by(designation='admin').first()

if admin==None:
    u1 = Login(username=params["admin_email"],password=params["admin_pass"],designation=params["admin_designation"])
    db.session.add(u1)
    db.session.commit()

    details = Register(firstname=params["admin_fname"], lastname=params["admin_lname"],
                       gender=params["admin_gender"], dob=params["admin_dob"], email=params["admin_email"],
                       ph_no=params["admin_phone_no"], address=params["admin_address"])
    db.session.add(details)
    db.session.commit()
