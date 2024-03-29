from flask import Flask, request, jsonify
import json
import os
from utils import database
from utils.movie import MovieModel
from utils.validators import CreateMovieValidator, UpdateMovieValidator

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
            start = request.args.get('start') if request.args.get('start') else 0
            offset = request.args.get('offset') if request.args.get('offset') else 0
            
            # Query param must be casted to string
            return database.get_movies(start=int(start), offset=int(offset))

        return database.get_movies()

    if request.method == 'POST':
        # If we get a bad request that means there is no JSON object
        req_body = request.json
        if req_body:

            # Validate the request body
            CreateMovieValidator().load(req_body)

            # Pass validated request body to create new document
            return database.create_movie(body=req_body)

    raise Exception()


# Request parameter <id> can be set to be a specific numeric type int, float
@app.route("/movies/<id>", methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def movies_by_id(id):  # Since we will be working with bson we need id to be a str
    if request.method == 'GET':
        return database.get_movie_by_id(id)

    if request.method == 'PUT' or request.method == 'PATCH':
        # Validate request
        UpdateMovieValidator().load(request.json)
        return database.update_movie_by_id(id, request.json)

    if request.method == 'DELETE':
        return database.remove_movie_by_id(id)


if __name__ == "__main__":
    app.run('localhost', port=5000, debug=True)
