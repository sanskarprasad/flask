# app/controllers/user_controller.py
import sys
sys.path.append("Z:/proj/sanskar/flask")
from app.models.user_model import User


from flask import jsonify, request

def get_all_users():
    users = User.get_all_users()
    return jsonify([{"id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users])

def get_user(user_id):
    user = User.get_user(user_id)
    if user:
        return jsonify({"id": str(user["_id"]), "name": user["name"], "email": user["email"]})
    return jsonify({"error": "User not found"}), 404

def create_user():
    data = request.json
    user_id = User.create_user(data)
    return jsonify({"id": user_id}), 201

def update_user(user_id):
    data = request.json
    User.update_user(user_id, data)
    return jsonify({"message": "User updated"}), 200

def delete_user(user_id):
    User.delete_user(user_id)
    return jsonify({"message": "User deleted"}), 204
