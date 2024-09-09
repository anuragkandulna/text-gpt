"""
Routes for user authentication and management.
"""

from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from datetime import datetime, timezone
from models.custom_logger import CustomLogger
from models.user import User


# Initialize constants: blueprint, loggers, etc
auth_bp = Blueprint('auth_bp', __name__)
bcrypt = Bcrypt()
LOGGER = CustomLogger(__name__, level=20).get_logger()


@auth_bp.route('/api/v1/login', methods=['POST'])
def login():
    """
    Login API for user authentication.
    """
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
        LOGGER.error(f'Exception in user login API/v1/login: {e}')
        return jsonify({"message": "An error occurred"}), 500


@auth_bp.route('/api/v1/register', methods=['POST'])
def register():
    """
    Register API for new user creation.
    """
    try:
        data = request.json

        username = data.get('username')
        password = data.get('password')

        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        User.create_new_user(
            username=username,
            password_hash=password_hash
        )

        LOGGER.info(f"{username} User registered successfully!")
        return jsonify({"message": f"{username} User registered successfully!"}), 201
    
    except Exception as e:
        LOGGER.error(f'Exception in new user registration API/v1/register: {e}')
        return jsonify({"message": "An error occurred during registration"}), 500
