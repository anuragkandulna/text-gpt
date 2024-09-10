import psycopg2
from psycopg2 import pool
from utils.custom_logger import CustomLogger


# Invoke LOGGER
LOGGER = CustomLogger(__name__, level=20).get_logger()


class DatabaseConnection:
    def __init__(self) -> None:
        """
        Set up a connection pool.
        """
        try:
            self.pool = psycopg2.pool.SimpleConnectionPool(
                minconn=1,
                maxconn=10,
                dbname="textgpt",
                user="baron",
                password="1234",
                host="localhost",
                port=5432
            )

            if self.pool:
                LOGGER.info("Connection pool created successfully.")
            else:
                LOGGER.error("Failed to create connection pool.")

        except Exception as ex:
            LOGGER.error(f"Failed to connect to the database: {ex}")
            raise


    def __enter__(self):
        """
        Enter the runtime context related to this connection object.
        """
        self.connection = self.pool.getconn()
        self.cursor = self.connection.cursor()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the runtime context related to this object, closing the connection.
        """
        self.close_connection()


    def execute_query(self, query: str, params: tuple = None) -> None:
        """
        Execute a query on the database.
        """
        self._execute(query, params)


    def bulk_insert(self, query: str, data: list) -> None:
        """
        Bulk insert data into the database.
        """
        self._execute(query, data, bulk=True)


    def fetch_data(self, query: str, params: tuple = None):
        """
        Fetch data from the database.
        """
        try:
            self.cursor.execute(query, params)
            data = self.cursor.fetchall()
            LOGGER.info(f"Fetched data from query: {query}")
            return data

        except Exception as ex:
            LOGGER.error(f"Failed to fetch data: {ex}")
            raise


    def health_check(self) -> bool:
        """
        Check the health of the database connection.
        """
        try:
            with self as db:
                result = db._execute("SELECT 1", fetch=True)
                return result is not None

        except Exception as ex:
            LOGGER.error(f"Health check failed: {ex}")
            return False


    def close_connection(self) -> None:
        """
        Close the database connection.
        """
        try:
            self.cursor.close()
            self.pool.putconn(self.connection)
            LOGGER.info("Database connection closed successfully.")

        except Exception as ex:
            LOGGER.error(f"Failed to close the database connection: {ex}")
            raise


    def close_pool(self) -> None:
        """
        Close all connections in the pool.
        """
        try:
            self.pool.closeall()
            LOGGER.info("Connection pool closed successfully.")

        except Exception as ex:
            LOGGER.error(f"Failed to close connection pool: {ex}")
            raise


    def _execute(self, query: str, params: tuple = None, bulk: bool = False, fetch: bool = False):
        """
        Helper method to execute queries.
        """
        try:
            if bulk:
                self.cursor.executemany(query, params)
            else:
                self.cursor.execute(query, params)

            if fetch:
                result = self.cursor.fetchall()
                LOGGER.info(f"Executed fetch query: {query}")
                return result
            self.connection.commit()
            LOGGER.info(f"Executed query: {query}")

        except Exception as ex:
            LOGGER.error(f"Failed to execute query: {ex}")
            self.connection.rollback()
            raise
