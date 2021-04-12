from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, ValidationError
from src.models import User

class LoginForm(FlaskForm):
	email = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField("Password", validators=[DataRequired()])
	remember_me = BooleanField("Remember me")
	submit = SubmitField("Sign in")

class RegisterForm(FlaskForm):
	first_name = StringField("First name", validators=[DataRequired(), Length(min=3, max=42)])
	last_name = StringField("Last name", validators=[DataRequired(), Length(min=3, max=42)])
	username = StringField("Username", validators=[DataRequired(), Length(min=3, max=62)])
	email = StringField("Email", validators=[DataRequired(),Email()])
	password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=42)])
	repeat_password = PasswordField("Repeat password", validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField("Sign up")

	def validate_username(self, username):
		if User.query.filter_by(username=username.data):
			raise ValidationError("That username is taken, please choose a different one.")

	def validate_email(self, email):
		if User.query.filter_by(email=email.data):
			raise ValidationError("That email is taken, please choose a different one.")