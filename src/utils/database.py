from pymongo import MongoClient
from flask import jsonify
from utils.movie import MovieModel

mongo_client = MongoClient(
    host='localhost',
    port=27017,
    username='root',  # Username of the database
    password='Sup3rS1mpl3'  # Password of the database
)

db = mongo_client['movie_catalog']
collection = db['movies']


def get_movies(start=0, offset=50):
    """Get all movies. Paginate accordingly. Return only id, title and year of a movie. Return 50 values by default"""

    res = jsonify()
    if (start >= offset) or (offset <= start):
        return jsonify({
            'ERROR': 'Internal server error. Make sure "start" and "offset" values are correct.'
        }), 500

    if offset >= 1000:
        return jsonify({
            'ERROR': "Cant return more than 1000 records at a time. Please set offset query param less than 1000"
        }), 500

    if start < 0:
        return jsonify({
            'ERROR': 'Query string error. "string value cannot be less than 0"'
        }), 500

    cursor = collection.find(
        {}, {"_id": True, "Title": True, "Year": True}).skip(start).limit(offset)

    # Response list
    res_arr = list()

    # Iterate over database objects and populate cursom JSON response
    for item in cursor:
        movie_object = MovieModel(**item)
        custom_json = {
            'Title': movie_object.title,
            'Year': movie_object.year,
            'id': movie_object.id
        }
        res_arr.append(custom_json)

    return jsonify(res_arr)


def create_movie(movie):
    """Insert a new movie into the database. use the movie model serialization."""
    pass


def get_movie_by_id(id):
    """Get a movie by id. Return all fields of a movie"""
    pass


def update_movie_by_id(id, movie_data):
    """Update the movie from the database by id"""
    pass


def remove_movie_by_id(id):
    """"Remove movie by id"""
    pass
