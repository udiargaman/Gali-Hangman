from flask import Blueprint, session, render_template, redirect, url_for, request, flash
from game_app.forms import GameForm
from game_app.game import theGame, oneQuestion

GAME_SIZE = 5
GAME_QLIST = "qlist"
GAME_WRONG = "wrong_count"
GAME_CURRENT = "current_question"

game_app = Blueprint("game_app", __name__)

# landing page
@game_app.route("/game")
def game():
    form = GameForm()
    user = session.get("user")

    # if there is a prev game, use it
    if GAME_CURRENT in session:
        current = session.get(GAME_CURRENT)
        wrong = session.get(GAME_WRONG)
        qlist_str = session.get(GAME_QLIST)

        game = theGame(qlist_str=qlist_str, current_question=current, wrong_answers=wrong)

        # read action and answer
        action = request.values.get("action", "")
        if action == "next":
            answer = int(request.values.get("answer", "-1"))
            if answer >= 0:
                game.submitAnswerAndMove(answer)

    else:  # new game
        game = theGame(game_size=GAME_SIZE)

    if game.game_on:    
        session[GAME_CURRENT] = game.current_question
        session[GAME_WRONG] = game.wrong_answers
        session[GAME_QLIST] = game.getQListString()

    # res is true while the game lasts, false when last Q is done. Q is the question object
    res, q = game.getCurrentQuestion()
    progress = str(game.current_question / game.game_size * 100)
      
    return render_template("game/game.html", user=user, form=form, game=game, question=q, progress=progress, last_round=not res, allowd_strikes=6)




