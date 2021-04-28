from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, g, session
from src import application, bcrypt,db, constants
from src.forms import LoginForm,RegisterForm
from src.models import User,DirectMessage
from src.utils import generate_user_tag, logout_user, load_user_contacts

@application.before_request
def get_user_info():
	g.user = None
	if 'user_id' in session:
		g.user = User.query.filter_by(id=session['user_id']).first()

@application.route("/")
@application.route("/home")
@application.route("/index")
def index():
	if not g.user:
		return redirect(url_for("login"))
	return render_template("index.html", title="Home", page_vars={'user_info': g.user}, next_page="home")

@application.route("/login",methods=['GET', 'POST'])
@application.route("/signin",methods=['GET', 'POST'])
def login():
	if g.user:
		return redirect(url_for('index'))
	form = LoginForm(request.form)
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			session['user_id'] = user.id
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('index'))
		else:
			flash("Login unsuccessful, Please try again.")
	return render_template("login.html", form=form)

@application.route("/register",methods=['GET', 'POST'])
@application.route("/signup",methods=['GET', 'POST'])
def register():
	if g.user:
		return redirect(url_for('index'))
	form = RegisterForm()
	if form.validate_on_submit():
		if constants.MAX_USERS_PER_USERNAME > len(User.query.filter_by(username=form.username.data).all()):
			tag = generate_user_tag(form.username.data)
			password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
			new_user = User(first_name=form.first_name.data, last_name=form.last_name.data,
				username=form.username.data,tag=tag,email=form.email.data, password=password)
			db.session.add(new_user)
			db.session.commit()
			flash("Successfuly registered.")
			return redirect(url_for('login'))
		else:
			flash("Register unsuccessful, too many people currently using the same username.")
	return render_template("register.html", form=form)

@application.route("/signout",methods=['GET', 'POST'])
@application.route("/logout",methods=['GET', 'POST'])
def logout():
	logout_user()
	return redirect(url_for('login'))

@application.errorhandler(404)
def page_not_found(e):
    return render_template("error.html")

@application.route("/app/<string:name>", methods=['POST', 'GET'])
def render_page(name):
	if request.method == "GET":
		return render_template("index.html", title="Home", page_vars={'user_info': g.user}, next_page=name)
	pages = {
		'home': render_template("home.html"),
		'explore': render_template("explore.html"),
		'notifications': render_template("notifications.html"),
		'contact': render_template("contact.html", contacts=load_user_contacts(), user=g.user),
		'profile': render_template("profile.html")
	}
	return pages.get(name, jsonify({'success': False, 'error': 'page couldn\'be found.'}))

@application.route("/directmessages/<int:userid>", methods=["POST"])
def retrieve_directmessages(userid):
	if 'user_id' in session:
		return jsonify([{"sender_id": message.origin_userid, "message": message.message} for message in DirectMessage.query.filter((DirectMessage.origin_userid.in_([userid, session['user_id']])) & (DirectMessage.other_userid.in_([userid, session['user_id']]))).all()])