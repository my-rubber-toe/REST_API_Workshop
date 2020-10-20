from db.db_connection import collection


def get_all_movies():
    return collection.find({
        "_id": 1
    })
