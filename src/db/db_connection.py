import json
from pymongo import MongoClient

# Establish database connection
client = MongoClient(
    host='localhost',
    port=27017,
    username='root',
    password='Sup3rS1mpl3'
)

# Get the database to use
db = client['movies']

# Get the collection to use
collection = db['streaming_services']