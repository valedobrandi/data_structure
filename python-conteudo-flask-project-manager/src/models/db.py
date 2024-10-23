import os
from pymongo import MongoClient

client = MongoClient(os.environ.get("MONGO_URL", "mongodb://localhost:27017"))

db = client.db_project[os.getenv("TEST_DATABASE", "db_project")]
