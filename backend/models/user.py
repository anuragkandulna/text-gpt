"""
User data model.
"""

import uuid
from datetime import datetime, timezone
from backend.utils.mongo_database import DatabaseConnection
from utils.custom_logger import CustomLogger


# Invoke LOGGER
LOGGER = CustomLogger(__name__, level=20).get_logger()
DB_CONN = DatabaseConnection()


class User:
    def __init__(self):
        self.user_id = ""
        self.username = ""
        self.email = ""
        self.password_hash = ""
        self.role = ""
        self.is_active = False
        self.created_at = 0
        self.updated_at = 0


    @staticmethod
    def _get_users_collection():
        """Get users collection."""
        return DB_CONN.get_collection(db_table='users')


    @staticmethod
    def generate_user_id():
        """Generate Unique ID for user and return in string format."""
        unique_id = uuid.uuid4()
        return str(unique_id)


    @classmethod
    def create_new_user(cls, username, password_hash):
        """
        Create 1 new user in database.
        """
        user_id = cls.generate_user_id()

        user_data = {
            "user_id": user_id,
            "username": username,
            "email": username,
            "password_hash": password_hash,
            "role": None,
            "is_active": True,
            "created_at": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z'),
            "updated_at": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')
        }
        
        LOGGER.info(f'Inserting one document into users table: {user_data}')
        return cls._get_users_collection().insert_one(user_data)


    @classmethod
    def get_user_id(cls, username):
        """
        Get userID for a username.
        """
        user_data = cls._get_users_collection().find_one({'username': username})
        LOGGER.info(f'Queried user data for {username}: {user_data}')

        if user_data:
            return user_data['user_id']

        return None


    @classmethod
    def find_by_username(cls, username):
        """
        Return single document object for username.
        """
        user_data = cls._get_users_collection().find_one({'username': username})
        LOGGER.info(f'Queried user data for {username}: {user_data}')

        if user_data:
            return {
                "username": user_data['username'],
                "email": user_data['email'],
                "password_hash": user_data['password_hash'],
                "is_active": user_data['is_active'],
            }

        return None
    