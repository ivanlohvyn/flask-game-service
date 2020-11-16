import json

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

with open("data.json", "r") as file:
    game_data = json.load(file)
players_data = game_data["data"]


@app.route("/api/v1/scores/send", methods=["POST", "GET"])
def write_player():
    if request.method == "POST":
        i = 0
        new_player = request.get_json()
        for i, player in enumerate(players_data):
            if player["scores"] >= new_player["scores"]:
                break
        else:
            i = i + 1
        players_data.insert(i, new_player)
        with open("data.json", "w") as file:
            json.dump(game_data, file, indent=4, ensure_ascii=False)
    return "Players_scores"


@app.route("/api/v1/scores/table", methods=["GET"])
def static_table():
    df = pd.read_json("data.json")
    pl = pd.json_normalize(df[::-1]["data"])
    return render_template("scores.html", dataframe=pl.to_html())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
