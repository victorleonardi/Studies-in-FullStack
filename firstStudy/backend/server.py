from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {'origins': '*'}})

collection = {
    "1": {
        "id": "1",
        "name": "LoL",
        "genre": "MOBA",
        "played": True
    },
    "2": {
        "id": "2",
        "name": "Dota",
        "genre": "MOBA",
        "played": False
    }
}


@app.route('/games', methods=['GET'])
def get_all_games():
    return jsonify(list(collection.values()))


@app.route('/games/<id>', methods=['GET'])
def get_game(id):
    return collection[id]


@app.route('/games', methods=['POST'])
def add_game():
    _data = request.get_json()
    game_to_add = {
        "name": _data["name"],
        "genre": _data["genre"],
        "played": _data["played"]
    }
    collection[str(len(collection)+1)] = game_to_add
    return game_to_add


@app.route('/games/<id>', methods=['DELETE'])
def delte_game(id):
    return collection.pop(id)


if __name__ == '__main__':
    app.run(debug=True)
