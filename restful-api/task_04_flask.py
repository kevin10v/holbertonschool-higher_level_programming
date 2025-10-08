#!/usr/bin/env python3
"""
task_04_flask.py
Minimal Flask API: routes, JSON responses, simple POST create.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store. Do NOT push test data with the solution.
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Simple health endpoint."""
    return "OK"


@app.route("/data", methods=["GET"])
def list_usernames():
    """Return a JSON list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return full object for a given username or an error JSON."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Create a new user.
    Body JSON example:
    {"username":"john","name":"John","age":30,"city":"New York"}
    """
    data = request.get_json(silent=True) or {}
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Store the whole object; include username in the stored payload.
    user_obj = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }
    users[username] = user_obj

    return jsonify({"message": "User added", "user": user_obj}), 201


if __name__ == "__main__":
    # For local runs: python3 task_04_flask.py
    app.run()
