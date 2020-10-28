from pymongo import MongoClient
from flask import jsonify
from utils.movie import MovieModel
from bson.objectid import ObjectId

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

    if offset >= 1000 or offset <= 0:
        return jsonify({
            'ERROR': "Cant return more than 1000 records at a time. Please set offset query param less than 1000"
        }), 500

    if start < 0:
        return jsonify({
            'ERROR': 'Query string error. "string value cannot be less than 0"'
        }), 500

    cursor = collection.find(
        {}, {"_id": True, "title": True, "year": True}).skip(start).limit(offset)

    # Response list
    res_arr = list()

    # Iterate over database objects and populate cursom JSON response
    for item in cursor:
        movie_object = MovieModel(**item)
        custom_json = {
            'title': movie_object.title,
            'year': movie_object.year,
            'id': movie_object.id
        }
        res_arr.append(custom_json)

    return jsonify(res_arr)


def create_movie(body):
    """Insert a new movie into the database. use the movie model serialization."""
    # Insert movie to the database
    created_item = collection.insert_one(body)

    return jsonify({
        'message': 'Movie successfully created!',
        # Must be cast to str(). Raises TypeError: Object of type ObjectId is not JSON serializable
        'id': str(created_item.inserted_id)
    })


def get_movie_by_id(id):
    """Get a movie by id. Return all fields of a movie"""
    movie_doc = collection.find_one(
        {'_id': ObjectId(id)})  # Returns one JSON document or None

    if movie_doc:
        # Serialize the ObjectID from the document. If this is not done, jsonify cannot build response
        movie_doc['_id'] = str(movie_doc['_id'])

        return jsonify(movie_doc), 200

    return jsonify({'message': 'Invalid document id!'}), 403


def update_movie_by_id(id, movie_data):
    """Update the movie from the database by id"""

    # If the movie_data is the same as in the database will not update the document
    movie_doc_updated = collection.update_one(
        {'_id': ObjectId(id)}, {"$set": movie_data})

    if movie_doc_updated.modified_count > 0:
        return jsonify(
            {
                'message': 'Successfully updated documents!',
                'updated_count': movie_doc_updated.modified_count,
            }
        )

    return jsonify(
        {
            'message': 'No document was updated!',
            'updated_count': movie_doc_updated.modified_count
        }
    )


def remove_movie_by_id(id):
    """"Remove movie by id"""
    deleted_movie = collection.delete_one({'_id': ObjectId(id)})

    return jsonify(
        {
            'message': 'Successfully deleted document!',
            'deleted_count': deleted_movie.deleted_count
        }
    )
