from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, ValidationError
from src.models import User

class LoginForm(FlaskForm):
	email = StringField("Email", validators=[DataRequired(), Email()],render_kw={"placeholder": "Email", "type": "email"})
	password = PasswordField("Password", validators=[DataRequired()],render_kw={"placeholder": "Password"})
	remember_me = BooleanField("Remember me")
	submit = SubmitField("Sign in")

class RegisterForm(FlaskForm):
	first_name = StringField("First name", validators=[DataRequired(), Length(min=3, max=42)],render_kw={"placeholder": "First name"})
	last_name = StringField("Last name", validators=[DataRequired(), Length(min=3, max=42)],render_kw={"placeholder": "Last name"})
	username = StringField("Username", validators=[DataRequired(), Length(min=3, max=62)],render_kw={"placeholder": "Username"})
	email = StringField("Email", validators=[DataRequired(),Email()],render_kw={"placeholder": "Email", "type": "email"})
	password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=42)],render_kw={"placeholder": "Password"})
	repeat_password = PasswordField("Repeat password", validators=[DataRequired(), EqualTo('password')],render_kw={"placeholder": "Confirm password"})
	submit = SubmitField("Sign up")

	'''def validate_username(self, username):
		if User.query.filter_by(username=username.data).first():
			raise ValidationError("That username is taken, please choose a different one.")''' # Username doesn't have to be unique since we're using tags too

	def validate_email(self, email):
		if User.query.filter_by(email=email.data).first():
			raise ValidationError("That email is taken, please choose a different one.")