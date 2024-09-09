"""Mongod DB connnection models"""

from pymongo import MongoClient
from pymongo.collection import Collection
from utils.custom_logger import CustomLogger

# Invoke LOGGER
LOGGER = CustomLogger(__name__, level=20).get_logger()

class DatabaseConnection:
    def __init__(self) -> None:
        """Connect to database textgpt."""
        try:
            self.client = MongoClient('mongodb+srv://baron:agxscoCGbSly2aXw@cluster91181.jkqew.mongodb.net/test?retryWrites=true&w=majority')
            self.db = self.client['textgpt']
            LOGGER.info("Connected to the database successfully.")
        except Exception as ex:
            LOGGER.error(f"Failed to connect to the database: {ex}")
            raise

    def __enter__(self):
        """Enter the runtime context related to this connection object."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the runtime context related to this object, closing the connection."""
        self.close_connection()

    def get_collection(self, db_table: str) -> Collection:
        """Get database collection object."""
        try:
            collection = self.db[db_table]
            LOGGER.info(f"Accessed collection: {db_table}")
            return collection
        except Exception as ex:
            LOGGER.error(f"Failed to access database {db_table} collection: {ex}")
            raise

    def close_connection(self) -> None:
        """Close the database connection."""
        try:
            self.client.close()
            LOGGER.info("Database connection closed successfully.")
        except Exception as ex:
            LOGGER.error(f"Failed to close the database connection: {ex}")
            raise

