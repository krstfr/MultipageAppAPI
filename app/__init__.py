from flask import Flask
from config import Config
from flask_login import LoginManager #for loging users in and maintaing a session
from flask_sqlalchemy import SQLAlchemy #this talks to our database for us 
from flask_migrate import Migrate #makes changing database a lot easier 

#---Instantiation
app = Flask(__name__)
#---name space of file. this passes the file into the flask application
app.config.from_object(Config)
#---init Login Manager
login = LoginManager(app)
login.login_view = 'login'
#---init the database from_object
db = SQLAlchemy(app)
#---init migrate
migrate = Migrate(app, db)


from app import routes 