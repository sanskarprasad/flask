# app/models/user_model.py
from bson.objectid import ObjectId
from app.utils.db import db

class User:
    collection = db['users']

    @staticmethod
    def create_user(data):
        result = User.collection.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    def get_user(user_id):
        return User.collection.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def get_all_users():
        return list(User.collection.find())

    @staticmethod
    def update_user(user_id, data):
        User.collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    @staticmethod
    def delete_user(user_id):
        User.collection.delete_one({"_id": ObjectId(user_id)})
