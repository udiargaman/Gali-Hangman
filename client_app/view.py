from flask import Blueprint, session, render_template, redirect, url_for, request, flash
from client_app.forms import LoginForm

client_app = Blueprint("Gali's Hangman", __name__)

# main page
@client_app.route("/")
def index():
    form = LoginForm()
    return render_template("index.html", form=form)

# order submission

