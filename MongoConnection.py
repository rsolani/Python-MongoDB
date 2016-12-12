from pymongo import MongoClient


class MongoConnection:
    _col_name = ""

    def __init__(self, col_name):
        self.col_name = col_name

    @property
    def get_collection(self):
        client = MongoClient("mongodb://")
        db = client.freepy
        return db[self.col_name]
