from flask import Blueprint, session, render_template, redirect, url_for, request, flash
from client_app.forms import LoginForm

client_app = Blueprint("hangman", __name__)

# landing page
@client_app.route("/", methods=["GET", "POST"])
def index():
    form = LoginForm()

    if form.validate_on_submit():
        user = form.user_id.data
        session["user"] = user

        return redirect(url_for("/game"))

    return render_template("client/index.html", form=form)

# leader board
@client_app.route("/board")
def leaderBoard():
    return render_template("client/board.html")

@client_app.route("/howto")
def howtoPlay():
    return render_template("/client/howto.html")

@client_app.route("/about")
def aboutMe():
    return render_template("/client/aboutme.html")

