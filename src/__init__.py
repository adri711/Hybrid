from flask import Flask, url_for
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt

application = Flask(__name__)
socketio = SocketIO(application, cors_allowed_origins="*")
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(application)

# Importing other modules
from src.routes import*
from src.models import*