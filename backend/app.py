from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://<username>:<password>@<cluster-address>/test?retryWrites=true&w=majority')
db = client['textgpt']  # Replace with your database name
users_collection = db['users']

# Authentication route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    print(f'User is trying to log in: {username} : {password}')

    # Find the user in the database
    user = users_collection.find_one({"username": username})

    if not user:
        print(f'User {username} not found in database.')
        return jsonify({"message": "User not found"}), 404

    # Debugging: Print the stored hash and compare with password input
    stored_hash = user['password_hash']
    print(f'Stored password hash: {stored_hash}')
    
    if bcrypt.check_password_hash(stored_hash, password):
        print('Password match!')
        return jsonify({"message": "Login successful!", "user_id": str(user['_id'])}), 200
    else:
        print('Password does not match.')
        return jsonify({"message": "Incorrect password"}), 403

# Register route (if you need to add new users)
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Hash the password
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    print(f'Registering user {username} with hash: {password_hash}')

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