"""
User data model.
"""

from datetime import datetime, timezone
from utils.custom_logger import CustomLogger
from utils.psql_database import DatabaseConnection


# Invoke LOGGER
LOGGER = CustomLogger(__name__, level=20).get_logger()


class User:
    def __init__(self):
        self.user_id = ""
        self.username = ""
        self.email = ""
        self.password_hash = ""
        self.role = ""
        self.is_active = False
        self.created_at = None
        self.updated_at = None


    @classmethod
    def create_new_user(cls, username, password_hash):
        """
        Create 1 new user in database.
        """
        created_at = datetime.now(timezone.utc)
        updated_at = created_at

        query = """
        INSERT INTO users (user_id, username, email, password_hash, role, is_active, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            username,
            username,
            password_hash,
            None,
            True,
            created_at,
            updated_at
        )

        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
            LOGGER.info(f'Inserted one user into users table: {username}')

        except Exception as ex:
            LOGGER.error(f'Failed to create new user: {ex}')
            raise


    @classmethod
    def get_user_id(cls, username):
        """
        Get userID for a username.
        """
        query = "SELECT user_id FROM users WHERE username = %s"
        params = (username,)

        try:
            with DatabaseConnection() as db:
                result = db.fetch_data(query, params)
            if result:
                user_id = result[0][0]
                LOGGER.info(f'Queried user ID for {username}: {user_id}')
                return user_id
            return None

        except Exception as ex:
            LOGGER.error(f'Failed to fetch user ID: {ex}')
            raise


    @classmethod
    def find_by_username(cls, username):
        """
        Return single document object for username.
        """
        query = """
        SELECT username, email, password_hash, is_active
        FROM users
        WHERE username = %s
        """
        params = (username,)

        try:
            with DatabaseConnection() as db:
                result = db.fetch_data(query, params)
            if result:
                user_data = result[0]
                user_info = {
                    "username": user_data[0],
                    "email": user_data[1],
                    "password_hash": user_data[2],
                    "is_active": user_data[3],
                }
                LOGGER.info(f'Queried user data for {username}: {user_info}')
                return user_info
            return None

        except Exception as ex:
            LOGGER.error(f'Failed to fetch user data: {ex}')
            raise
