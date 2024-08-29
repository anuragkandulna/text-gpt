from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from datetime import datetime, timezone
from models.custom_logger import CustomLogger 
from models.user import User


# Defined defaults
app = Flask(__name__)
bcrypt = Bcrypt(app)
LOGGER = CustomLogger(__name__, level=20).get_logger()
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/api/test', methods=['GET'])
def test():
    LOGGER.info('Test route hit!!!')
    return jsonify({"message": "Test route is working!"}), 200


# Authentication route
@app.route('/api/v1/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        user_data = User.find_by_username(username=username)
        if not user_data:
            LOGGER.info(f'{username} not found in database')
            return jsonify({"message": f"{username} User not found!"}), 404

        stored_hash = user_data.get('password_hash')

        if bcrypt.check_password_hash(stored_hash, password):
            current_ts = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')
            LOGGER.info(f'{current_ts}: {username} successfully logged in')
            return jsonify({"message": f"{username} Login successful!"}), 200

        else:
            LOGGER.info(f'{current_ts}: {username} Incorrect password!!!')
            return jsonify({"message": "Incorrect password!!!"}), 403

    except Exception as e:
        LOGGER.info(f'Exception in user login API/v1/login: {e}')
        return jsonify({"message": "An error occurred"}), 500


# Register route (if you need to add new users)
@app.route('/api/v1/register', methods=['POST'])
def register():
    try:
        data = request.json

        username = data.get('username')
        password = data.get('password')

        # Hash the password
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        User.create_new_user(
            username=username,
            password_hash=password_hash
        )

        LOGGER.info(f"{username} User registered successfully!")
        return jsonify({"message": f"{username} User registered successfully!"}), 201
    
    except Exception as e:
        LOGGER.info(f'Exception in new user registration API/v1/register: {e}')
        return jsonify({"message": "An error occurred during registration"}), 500

if __name__ == '__main__':
    app.run(debug=True)
