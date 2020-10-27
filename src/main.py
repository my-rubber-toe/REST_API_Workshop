from flask import Flask, request, jsonify
import json
import os
from utils import database
from utils.movie import MovieModel

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
        3: '/movies?start=<int>&offset=<int>',
    }

    return jsonify(available_routes), 200


@app.route("/movies", methods=['GET', 'POST'])
def movies_endpoint():
    if request.method == 'GET':
        if request.args:
            start = int(request.args.get('start')) if request.args.__contains__('start') else 0
            offset = int(request.args.get('offset')) if request.args.__contains__('start') else 0
            return database.get_movies(start=start, offset=offset)

        return database.get_movies()
    
    if request.method == 'POST':
        # If we get a bad request that means there is no JSON object
        req_body = request.json
        if req_body:
            return database.create_movie(body=req_body)
            

    raise Exception()


# Request parameter <id> can be set to be a specific numeric type int, float
@app.route("/movies/<id>")
def movies_by_id(id):  # Since we will be josking with bson we need it to be a str
    return database.get_movie_by_id(id)


if __name__ == "__main__":
    app.run('localhost', port=5000, debug=True)
