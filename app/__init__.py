from flask import Flask
from config import Config

#Instantiation
app = Flask(__name__)
#name space of file. this passes the file into the flask application
app.config.from_object(Config)

from app import routes 