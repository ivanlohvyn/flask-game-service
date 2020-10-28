import json
from operator import itemgetter

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/api/v1/scores/send", methods=["POST"])
def write_json(filename="data.json"):
    if request.method == "POST":
        game_data = request.get_json()

        with open(filename, "w") as file:
            json.dump(game_data, file, indent=2, ensure_ascii=False)
    return "<h1>Game scores</h1>"


@app.route("/api/v1/scores/table", methods=["GET"])
def static_table():
    with open("data.json", "r") as file:
        rating = json.load(file)
        for player in rating.values():
            leaders = sorted(player, key=itemgetter("scores"), reverse=True)
    return render_template("scores.html", leaders=leaders)


if __name__ == "__main__":
    app.run(debug=True)
