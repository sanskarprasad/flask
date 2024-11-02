# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://username:password@localhost:27017/testdb")
