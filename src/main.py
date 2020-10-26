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
    if request.args:
        try:
            start = request.args['start']
            offset = request.args['offset']

            # extract info from the database with start and offset
            # https://www.codementor.io/@arpitbhayani/fast-and-efficient-pagination-in-mongodb-9095flbqr

        except KeyError as error:
            print(error)
            return "Invalid query string!"

    # movie_arr = None

    # with open(os.path.join(os.path.dirname(__file__), './movies.json')) as f:
    #     movie_arr = json.load(f)

    #     return jsonify(movie_arr), 200

    return "No args"


@app.route("/movies/<int:id>")
def movie_by_id(id):
    pass


if __name__ == "__main__":
    app.run('localhost', port=5000, debug=True)
