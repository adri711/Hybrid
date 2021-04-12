from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, g, session
from src.forms import LoginForm,RegisterForm
from src import application, bcrypt,db
from src.models import *

@application.route("/")
@application.route("/home")
@application.route("/index")
def index():
	if not hasattr(g, 'user_id'):
		return redirect(url_for("login"))
	return render_template("index.html", title="Home")

@application.route("/login")
@application.route("/signin")
def login():
	if hasattr(g, 'user_id'):
		return redirect(url_for(index))
	form = LoginForm(request.form)
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			session['user_id'] = user.id
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for(index))
		else:
			flash("Login unsuccessful, Please try again.")
	return render_template("login.html", form=form)

@application.route("/register")
@application.route("/signup")
def register():
	if hasattr(g, 'user_id'):
		return redirect(url_for(index))
	form = RegisterForm(request.form)
	if form.validate_on_submit():
		password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		new_user = User(first_name=form.first_name.data, last_name=form.last_name.data,
			username=form.username.data,email=form.email.data, password=password)
		db.session.add(new_user)
		db.session.commit()
		flash("Successfuly registered.")
		return redirect(url_for(login))
	return render_template("register.html", form=form)

@application.route("/app/<string:name>", methods=['GET', 'POST'])
def render_page(name):
	switch = {
		'home': render_template("home.html"),
		'explore': render_template("explore.html"),
		'notifications': render_template("notifications.html"),
		'contact': render_template("contact.html"),
		'profile': render_template("profile.html")
	}
	return switch.get(name, jsonify({'success': False, 'error': 'page couldn\'be found.'}))