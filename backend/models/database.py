"""Mongod DB connnection models"""

from pymongo import MongoClient

class DatabaseClient:
    def __init__(self) -> None:
        self.client = MongoClient('mongodb+srv://baron:agxscoCGbSly2aXw@cluster91181.jkqew.mongodb.net/test?retryWrites=true&w=majority')
        self.db = self.client['textgpt']


    def getTable(self, db_table):
        """Get object to entire database table."""
        try:
            self.collection = self.db[db_table]
            return self.collection
        except Exception as ex:
            print(f'Failed to access database {db_table} table: {ex}')
