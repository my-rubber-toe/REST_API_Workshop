from pymongo import MongoClient
from movie import MovieModel

mongo_client = MongoClient(
    host='localhost',
    port=27017,
    username='root',  # Username of the database
    password='Sup3rS1mpl3'  # Password of the database
)

db = mongo_client['movie_catalog']
collection = db['movies']


def get_movies():
    """Get all movies. Paginate accordingly. Return only id, title and year of a movie."""
    pass


def create_movie(movie: MovieModel):
    """Insert a new movie into the database. use the movie model serialization."""
    pass


def get_movie_by_id(id):
    """Get a movie by id. Return all fields of a movie"""
    pass


def update_movie_by_id(id, movie_data: MovieModel):
    """Update the movie from the database by id"""
    pass


def remove_movie_by_id(id):
    """"Remove movie by id"""
    pass
