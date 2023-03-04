from flask import render_template, redirect
from flaskr import app
from flaskr.utils.games import (
    query_games,
    get_game_name,
    get_all_times_in_game,
    query_game_by_name,
)


@app.route("/games")
def get_games():
    games = query_games()
    if games is None:
        return render_template("games.html", games_exist=False)
    return render_template("games.html", games=games, games_exist=True)


@app.route("/games/<int:game_id>")
def get_game_by_id(game_id):
    try:
        game_id = int(game_id)
        game_name = get_game_name(game_id)
    except ValueError:
        return render_template(
            "error.html", message="Incorrect id, id not found or incorrect value"
        )
    times = get_all_times_in_game(game_id)
    return render_template(
        "game_id.html", times_exist=True, game_name=game_name, times=times
    )


@app.route("/api/game/<string:game_name>")
def get_game_by_name(game_name: str):
    try:
        game_name = str(game_name).replace("%20", " ")
        game_id = query_game_by_name(game_name)
        return redirect(f"/games/{game_id}")
    except ValueError as e:
        return render_template("error.html", message=f"Error fetching game name, {e}")
