"""
Routes for user authentication and management.
"""

from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from datetime import datetime, timezone, timedelta
import jwt
import os
from functools import wraps
from constants.config import JWT_SECRET_KEY
from utils.custom_logger import CustomLogger
from models.user import User


# Initialize constants: blueprint, loggers, etc
auth_bp = Blueprint('auth_bp', __name__)
bcrypt = Bcrypt()
LOGGER = CustomLogger(__name__, level=20, log_file="textgpt_auth.log").get_logger()


def generate_token(username):
    """
    Generate JWT token with expiry.
    """
    try:
        payload = {
            "username": username,
            "exp": datetime.utcnow() + timedelta(hours=12)  # Token expires in 12 hours
        }
        token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
        return token
    except Exception as e:
        LOGGER.error(f"Error generating token: {e}")
        return None


def token_required(f):
    """
    Decorator to validate JWT token before accessing protected routes.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            token = token.split("Bearer ")[1]  # Extract token
            decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
            request.username = decoded_token["username"]
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401
        return f(*args, **kwargs)
    return decorated


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
            token = generate_token(username)
            current_ts = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')
            LOGGER.info(f'{current_ts}: {username} successfully logged in')

            return jsonify({
                "message": f"{username} Login successful!",
                "token": token
            }), 200

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


@auth_bp.route('/api/v1/protected', methods=['GET'])
@token_required
def protected_route():
    """
    Example protected route that requires a valid JWT token.
    """
    return jsonify({"message": f"Hello, {request.username}! You have access to this protected resource."}), 200
