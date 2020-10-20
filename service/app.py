from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route("/", methods=["POST"])
def get_data(filename="data.json"):
    if request.method == "POST":
        game_data = request.get_json()
        with open(filename, "w") as file:
            json.dump(game_data, file, indent=2, ensure_ascii=False)
    return '<h1>Players</h1>'

if __name__ == "__main__":
    app.run(debug=True)