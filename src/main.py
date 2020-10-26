from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)


@app.route("/")
def main_route():
    """
        Main route. Returns a list of the available endpoints on this service.
    """
    available_routes = {
        0: '/',
        1: '/movies',
        2: '/movies/<id>',
        3: '/movies?year=<int>&lt=<bool>&mt=<bool>',
        4: '/movies?genre=<string>',
        5: '/movies?runtime=<int>&lt=<bool>&mt=<bool>',
        6: '/movies?servicename=<string>'
    }

    return jsonify(available_routes), 200


@app.route("/movies")
def movies():
    """
        Accessing all movies. Perform request operations based on the provided query string.
    """
    movie_arr = None

    with open(os.path.join(os.path.dirname(__file__), './movies.json')) as f:
        movie_arr = json.load(f)

        return jsonify(movie_arr), 200


@app.route("/movies/<int:id>")
def movie_by_id(id):
    with open(os.path.join(os.path.dirname(__file__), './movies.json')) as f:
        movie_arr = json.load(f)
        for m in movie_arr:
            if m['id'] == id:
                return jsonify(m), 200
        return f"Unable to retrieve movie. Invalid id={id}"


if __name__ == "__main__":
    app.run('localhost', port=5000, debug=True)
