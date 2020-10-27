import json
from pymongo import MongoClient
from bson import ObjectId


class MovieModel:
    def __init__(self, **kwargs):
        self.id: objectid = kwargs['_id']
        self.title: str = kwargs['Title']
        self.year: int = kwargs['Year']
        self.age: int = kwargs['Age']
        self.imdb: float = kwargs['IMDb']
        self.rotten_tomatoes: str = kwargs['Rotten Tomatoes']
        self.netflix: int = kwargs['Netflix']
        self.hulu: int = kwargs['Hulu']
        self.prime_video: int = kwargs['Prime Video']
        self.disney_plus: int = kwargs['Disney+']
        self.type = kwargs['Type']
        self.directors: list = kwargs['Directors']
        self.genres: list = kwargs['Genres']
        self.country: str = kwargs['Country']
        self.language: str = kwargs['Language']
        self.runtime: int = kwargs['Runtime']

    def to_json(self):
        return {
            "_id": self.id,
            "Title": self.title,
            "Year": self.year,
            "Age": self.age,
            "IMDb": self.imdb,
            "Rotten Tomatoes": self.rotten_tomatoes,
            "Netflix": self.netflix,
            "Hulu": self.hulu,
            "Prime Video": self.prime_video,
            "Disney+": self.disney_plus,
            "Type": self.type,
            "Directors": self.directors,
            "Genres": self.genres,
            "Country": self.country,
            "Language": self.language,
            "Runtime": self.runtime
        }

    def __str__(self):
        return f"<MovieModel('Title':{self.title})>"


client = MongoClient(
    host='localhost',
    port=27017,
    username='root',  # Username of the database
    password='Sup3rS1mpl3'  # Password of the database
)


db = client['movie_catalog']  # create database if it exists
collection = db['movies']

# Returns cursor object to navigate  all the data from the documents
# movie_arr = collection.find({})
# movie_count = collection.count_documents(
#     {})  # count all documents with no filter
# print(movie_count)

# one_movie = collection.find({'Title': 'Inception'})
# for m in one_movie:
#     print(MovieModel(**m).to_json())


# Find by filter
# print(collection.find_one({'_id': ObjectId('5f97a41812568277447a423b')}))
# for m in movie_arr:
#     a_movie = MovieModel(**m)
#     print(a_movie.id)

# Update by filter
# my_query = {'_id': ObjectId('5f97a41812568277447a423b')}
# my_values = {"$set": {'Title':'I am a new title'}}
# collection.update_one(my_query, my_values)

results = collection.find({}, {"_id": 0, "Title": 1}).skip(10).limit(3)
for x in results:
    print(x)


client.close()
