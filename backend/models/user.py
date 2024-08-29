"""
User data model.
"""

import bcrypt
from datetime import datetime, timezone
from database import DatabaseConnection as db
from custom_logger import CustomLogger


# Invoke LOGGER
LOGGER = CustomLogger(__name__, level=20).get_logger()


class User:
    def __init__(self, username, password=None, password_hash=None):
        self.username = username
        self.email = username
        self.password_hash = password_hash or self.hash_password(password=password)
        self.role = None
        self.is_active = False
        self.created_at = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')
        self.updated_at = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')


    def _get_users_collection():
        """Get users collection."""
        return db.get_collection(db_table='users')


    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


    def create_new_user(self):
        """
        Create 1 new user in database.
        """
        user_data = {
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "role": self.role,
            "is_active": True
        }
        
        LOGGER.info(f'Inserting one document into users table: {user_data}')
        return self._get_users_collection.insert_one(user_data)


    @classmethod
    def find_by_username(cls, username):
        """
        Return single document object for username.
        """
        user_data = cls._get_users_collection().find_one({'username': username})
        LOGGER.info(f'Queried user data for {username}: {user_data}')

        if user_data:
            
            return cls(
                username=user_data['username'],
                email=user_data['email'],
                password_hash=user_data['password_hash'],
                is_active=user_data['is_active'],
            )
        return None
