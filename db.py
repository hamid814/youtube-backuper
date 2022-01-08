from pymongo import MongoClient

from decouple import config

client = MongoClient(config('MONGO_URI'))

db = client['youtube']
collection = db['ids']

def save_one(video):
  collection.insert_one(video)

def save_many(videos):
  collection.insert_many(videos)

def clear_ids():
  res = collection.delete_many({})
  print(res.deleted_count, ' items were deleted.')
  