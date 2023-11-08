from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Initializing the web app
app = Flask(__name__)
app.config['SECRET_KEY'] = '150156a681c95a8ef057a4a5'

# Connecting with database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/employee'

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://dhairya:password@my_flask_assignment_db:3306/codingthunder"
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://python:password@python_flask_db:3306/employee"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://python:password@0.0.0.0/employee"

db = SQLAlchemy(app)



bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

from app_files.routes import routes