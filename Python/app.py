import time
from pymongo import MongoClient

# Connect to the MongoDB container using its container network name
client = MongoClient("mongodb://db:27017/")
db = client.cloud_db
visits_collection = db.visits

print("Connecting to MongoDB...", flush=True)
time.sleep(2)  # Give MongoDB a moment to boot up

# Insert a new visit log entry
visits_collection.insert_one({"timestamp": time.time()})
count = visits_collection.count_documents({})

print(f"🚀 Success! This script has run {count} times.", flush=True)