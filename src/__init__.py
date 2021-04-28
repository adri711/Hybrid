from flask import Flask, url_for
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

application = Flask(__name__)
socketio = SocketIO(application, cors_allowed_origins="*")
application.config['SECRET_KEY'] = "my secret key"
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)
Migrate(application, db)
bcrypt = Bcrypt(application)
online_users = {}

# Importing other modules
from src.cli_commands import *
from src.routes import *
from src.models import *
from src.network import *