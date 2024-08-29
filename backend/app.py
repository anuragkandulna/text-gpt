from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from flask_cors import CORS
from datetime import datetime, timezone

app = Flask(__name__)
bcrypt = Bcrypt(app)

# CORS(app)  # This will enable CORS for all routes
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})
CORS(app, resources={r"/*": {"origins": "*"}})


# Connect to MongoDB Atlas
# mongodb+srv://baron:agxscoCGbSly2aXw@cluster91181.jkqew.mongodb.net/test?retryWrites=true&w=majority
client = MongoClient('mongodb+srv://baron:agxscoCGbSly2aXw@cluster91181.jkqew.mongodb.net/test?retryWrites=true&w=majority')
db = client['textgpt']  # Replace with your database name
users_collection = db['users']


@app.route('/test', methods=['GET'])
def test():
    print("Test route hit!")
    return jsonify({"message": "Test route is working!"}), 200


# Authentication route
@app.route('/api/v1/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        user = users_collection.find_one({"username": username})
        if not user:
            return jsonify({"message": "User not found"}), 404

        stored_hash = user.get('password_hash')

        if bcrypt.check_password_hash(stored_hash, password):
            print(f'{username} successfully logged in on {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')}')
            return jsonify({"message": "Login successful!", "user_id": str(user['_id'])}), 200
        else:
            return jsonify({"message": "Incorrect password"}), 403
    except Exception as e:
        print(f'Exception in user login API/login: {e}')
        return jsonify({"message": "An error occurred"}), 500

# Register route (if you need to add new users)
@app.route('/api/v1/register', methods=['POST'])
def register():
    try:
        data = request.json

        username = data.get('username')
        email = data.get('username')
        password = data.get('password')
        # first_name = data.get('first_name')
        # last_name = data.get('last_name')
        created_at = data.get('created_at')
        updated_at = data.get('updated_at')

        # Hash the password
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        # Prepare the user document to insert into MongoDB
        user = {
            "username": username,
            "email": email,
            "password_hash": password_hash,
            # "first_name": first_name,
            # "last_name": last_name,
            "role": "user",
            "is_active": True,
            "created_at": created_at,
            "updated_at": updated_at
        }

        # Insert the user into the database
        result = users_collection.insert_one(user)

        # Return success response
        return jsonify({"message": "User registered successfully!"}), 201
    
    except Exception as e:
        print(f'Exception in new user registration API/register: {e}')
        return jsonify({"message": "An error occurred during registration"}), 500

if __name__ == '__main__':
    app.run(debug=True)