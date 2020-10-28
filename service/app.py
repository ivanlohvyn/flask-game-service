import json
from operator import itemgetter

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/api/v1/scores/send", methods=["POST", "GET"])
def write_json(filename="data.json"):
    if request.method == "POST":
        game_data = request.get_json()
        with open(filename, "w") as file:
            json.dump(game_data, file, indent=2, ensure_ascii=False)
    return "<h1>Game scores</h1>"


@app.route("/api/v1/scores/table", methods=["GET"])
def static_table():
    file = open("data.json")
    rating = json.load(file)
    for player in rating.values():
        highscores = sorted(player, key=itemgetter("scores"), reverse=True)
    print(highscores)
    file.close()
    return render_template("scores.html", rating=rating, highscores=highscores)


if __name__ == "__main__":
    app.run(debug=True)
