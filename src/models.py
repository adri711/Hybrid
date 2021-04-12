from flask_sqlalchemy import SQLAlchemy
from src import db
from datetime import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(62), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	first_name = db.Column(db.String(42), nullable=False)
	last_name = db.Column(db.String(42), nullable=False)
	password = db.Column(db.String(320), nullable=False)
	date_registered = db.Column(db.DateTime, default=datetime.now)

	def __repr__(self):
		return f""