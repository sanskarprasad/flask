# app/utils/db.py
from pymongo import MongoClient
from app.config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_database()  # Default database (defined in URI)
