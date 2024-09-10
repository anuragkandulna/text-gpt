import psycopg2
from psycopg2 import sql
from contextlib import contextmanager
from utils.custom_logger import CustomLogger


# Invoke LOGGER
LOGGER = CustomLogger(__name__, level=20).get_logger()


class DatabaseConnection:
    def __init__(self) -> None:
        """Connect to the PostgreSQL database 'textgpt'."""
        try:
            self.connection = psycopg2.connect(
                dbname="textgpt",
                user="baron",
                password="1234",
                host="localhost",  # or the IP address of your PostgreSQL server
                port="5432"  # default port for PostgreSQL
            )
            self.cursor = self.connection.cursor()
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


    def execute_query(self, query: str, params: tuple = None) -> None:
        """Execute a query on the database."""
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            LOGGER.info(f"Executed query: {query}")
        except Exception as ex:
            LOGGER.error(f"Failed to execute query: {ex}")
            self.connection.rollback()
            raise


    def fetch_data(self, query: str, params: tuple = None):
        """Fetch data from the database."""
        try:
            self.cursor.execute(query, params)
            data = self.cursor.fetchall()
            LOGGER.info(f"Fetched data from query: {query}")
            return data
        except Exception as ex:
            LOGGER.error(f"Failed to fetch data: {ex}")
            raise


    def close_connection(self) -> None:
        """Close the database connection."""
        try:
            self.cursor.close()
            self.connection.close()
            LOGGER.info("Database connection closed successfully.")
        except Exception as ex:
            LOGGER.error(f"Failed to close the database connection: {ex}")
            raise
