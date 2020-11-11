import json

from flask import Flask, request

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


if __name__ == "__main__":
    app.run(debug=True)
