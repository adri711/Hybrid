from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from src import application

@application.route("/")
@application.route("/home")
@application.route("/index")
def index():
    return render_template("index.html", title="Home")

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