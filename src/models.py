from flask_sqlalchemy import SQLAlchemy
from src import db
from datetime import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(62), unique=False, nullable=False)
	tag = db.Column(db.String(4), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	first_name = db.Column(db.String(42), nullable=False)
	last_name = db.Column(db.String(42), nullable=False)
	password = db.Column(db.String(320), nullable=False)
	date_registered = db.Column(db.DateTime, default=datetime.now)
	orgfriend = db.relationship("Friendship", backref="origin", lazy=True, foreign_keys="Friendship.origin_userid")
	otherfriend = db.relationship("Friendship", backref="other", lazy=True, foreign_keys="Friendship.other_userid")

	def __repr__(self):
		return f"User({self.username} #{self.tag}, {self.email}, {self.first_name} {self.last_name})"

class Friendship(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	origin_userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	other_userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Friendship ({User.query.filter_by(id=self.origin_userid).first().username} , {User.query.filter_by(id=self.other_userid).first().username})"

class DirectMessage(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	origin_userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	other_userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	message = db.Column(db.String(325), nullable=False)

	def __repr__(self):
		return f"Message from {User.query.filter_by(id=self.origin_userid).first().username} to {User.query.filter_by(id=self.other_userid).first().username}: {self.message}"