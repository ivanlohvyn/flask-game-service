import json

from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("service.config.Config")
db = SQLAlchemy(app)


class Player(db.Model):
    __tablename__ = "players"

    player_id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(128), unique=True, nullable=False)
    player_points = db.Column(db.Integer)

    def __init__(self, player_name, player_points):
        self.player_name = player_name
        self.player_points = player_points


@app.route("/api/v1/players", methods=["POST"])
def add_player():
    player_name = request.form["player_name"]
    player_points = request.form["player_points"]
    new_player = Player(player_name=player_name, player_points=player_points)
    db.session.add(new_player)
    db.session.commit()
    return "New player added"


@app.route("/players_update", methods=["PUT"])
def update_player():
    player_id = int(request.form["player_id"])
    player = Player.query.filter_by(player_id=player_id).first()
    if player:
        player.player_name = request.form["player_name"]
        player.player_points = request.form["player_points"]
        db.session.commit()
        return "Player updated"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
