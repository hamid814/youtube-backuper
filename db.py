from pymongo import MongoClient

from decouple import config

client = MongoClient(config('MONGO_URI'))

db = client['youtube']
collection = db['videos']

def save_one(video):
  collection.insert_one(video)
