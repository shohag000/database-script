from pymongo import MongoClient
client = MongoClient('localhost', 27017)
#database name
db = client['shipyard']

source_collection = db["users"]
destination_collection = db["abcd"]

source_collection_cursor = source_collection.find()

for data in source_collection_cursor:
      destination_collection.insert_one(data)