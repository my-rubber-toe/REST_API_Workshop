import json
from pymongo import MongoClient

client = MongoClient(
    host='localhost',
    port=27017,
    username='root',
    password='Sup3rS1mpl3'
)
db = client['movies']
collection = db['streaming_services']
collection.drop()


with open('movies.json') as f:
    file_data = json.load(f)
    total = len(file_data)
    count = 0
    for x in file_data:
        collection.insert_one(x)
        print('Uploaded ' + "{:.2f}".format(count/total * 100))
        count =  count + 1

client.close()