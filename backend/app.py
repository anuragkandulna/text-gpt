### Basic app to test backend as of now.

from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['textgpt']  # Replace with your database name
users_collection = db['users']

# Authentication route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    print(f'User is tring to login in: {username} : {password}')

    # Find the user in the database
    user = users_collection.find_one({"username": username})

    if not user:
        return jsonify({"message": "User not found"}), 404

    if not bcrypt.check_password_hash(user['password_hash'], password):
        return jsonify({"message": "Incorrect password"}), 403

    return jsonify({"message": "Login successful!", "user_id": str(user['_id'])}), 200

# Register route (if you need to add new users)
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Hash the password
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user
    user = {
        "username": username,
        "email": email,
        "password_hash": password_hash,
        "first_name": data.get('first_name'),
        "last_name": data.get('last_name'),
        "role": "user",
        "is_active": True,
        "created_at": data.get('created_at'),
        "updated_at": data.get('updated_at')
    }

    # Insert the user into the database
    users_collection.insert_one(user)

    return jsonify({"message": "User registered successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
