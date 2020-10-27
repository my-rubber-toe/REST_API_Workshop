import json
from pymongo import MongoClient

from bson import objectid


class MovieModel:
    def __init__(self, **kwargs):
        # self.id: objectid = kwargs['_id']
        self.title: str = kwargs['Title']
        self.year: int = kwargs['Year']
        self.age: int = kwargs['Age']
        self.imdb: float = kwargs['IMDb']
        self.rotten_tomatoes: str = kwargs['Rotten Tomatoes']
        self.netflix: int = kwargs['Netflix']
        self.hulu: int = kwargs['Hulu']
        self.prime_video: int = kwargs['Prime Video']
        self.disney_plus: int = kwargs['Disney+']
        # self.type = kwargs['Type']
        self.directors: list = kwargs['Directors']
        self.genres: list = kwargs['Genres']
        self.country: str = kwargs['Country']
        self.language: str = kwargs['Language']
        self.runtime: int = kwargs['Runtime']

    def __str__(self):
        return f"<MovieModel('title':{self.title})>"


client = MongoClient(
    host='localhost',
    port=27017,
    username='root',  # Username of the database
    password='Sup3rS1mpl3'  # Password of the database
)


db = client['movie_catalog']  # create database if it exists
collection = db['movies']
collection.drop()


with open('movies.json') as f:
    file_data = json.load(f)
    total = len(file_data)
    count = 0
    for x in file_data:
        movie = MovieModel(**x)
        print(movie)

        collection.insert_one(x)
        print('Uploaded ' + "{:.2f}".format(count/total * 100))
        count = count + 1

client.close()
