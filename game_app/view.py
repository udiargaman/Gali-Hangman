from flask import Blueprint, session, render_template, redirect, url_for, request, flash
from game_app.forms import GameForm

game_app = Blueprint("game_app", __name__)

# landing page
@game_app.route("/game")
def game():
    form = GameForm()
    return render_template("game_app/game.html", form=form)

