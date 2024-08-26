from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)
bcrypt = Bcrypt(app)

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
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        print(f'Received JSON data: {data}')
        
        username = data.get('username')
        password = data.get('password')

        print(f'Attempting to log in user: {username} with password: {password}')

        user = users_collection.find_one({"username": username})
        if not user:
            print(f'User {username} not found.')
            return jsonify({"message": "User not found"}), 404

        stored_hash = user.get('password_hash')
        print(f'Stored hash: {stored_hash}')

        if bcrypt.check_password_hash(stored_hash, password):
            print('Password matches.')
            return jsonify({"message": "Login successful!", "user_id": str(user['_id'])}), 200
        else:
            print('Password does not match.')
            return jsonify({"message": "Incorrect password"}), 403
    except Exception as e:
        print(f'An error occurred: {str(e)}')
        return jsonify({"message": "An error occurred"}), 500

# Register route (if you need to add new users)
@app.route('/register', methods=['POST'])
def register():
    try:
        # Step 1: Capture the incoming JSON data
        data = request.json
        print(f"Received data: {data}")

        # Step 2: Extract user details from the data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        created_at = data.get('created_at')
        updated_at = data.get('updated_at')

        # Debugging: Print extracted values to ensure they are correct
        print(f"Extracted username: {username}")
        print(f"Extracted email: {email}")
        print(f"Extracted password: {password}")
        print(f"Extracted first name: {first_name}")
        print(f"Extracted last name: {last_name}")
        print(f"Extracted created_at: {created_at}")
        print(f"Extracted updated_at: {updated_at}")

        # Step 3: Hash the password
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        print(f"Generated password hash: {password_hash}")

        # Step 4: Prepare the user document to insert into MongoDB
        user = {
            "username": username,
            "email": email,
            "password_hash": password_hash,
            "first_name": first_name,
            "last_name": last_name,
            "role": "user",
            "is_active": True,
            "created_at": created_at,
            "updated_at": updated_at
        }

        # Debugging: Print the user document before insertion
        print(f"User document to be inserted: {user}")

        # Step 5: Insert the user into the database
        result = users_collection.insert_one(user)
        print(f"User inserted with _id: {result.inserted_id}")

        # Return success response
        return jsonify({"message": "User registered successfully!"}), 201
    
    except Exception as e:
        # Handle and print any exceptions that occur
        print(f"An error occurred during registration: {str(e)}")
        return jsonify({"message": "An error occurred during registration"}), 500

if __name__ == '__main__':
    app.run(debug=True)