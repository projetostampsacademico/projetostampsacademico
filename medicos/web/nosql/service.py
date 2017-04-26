from pymongo import MongoClient
from singleton import Singleton
from pprint import pprint
from bson.json_util import dumps

@Singleton
class MongoService:

    def __init__(self):
        client = MongoClient('mongodb://heroku_6c04n1s3:eg0rtjdqtmf8ukmmo3pfflqdbe@ds161630.mlab.com:61630/heroku_6c04n1s3')
        self.db = client.heroku_6c04n1s3

    def collection_names(self):
        return self.db.collection_names()

    def fetch_data(self, collection):
        return dumps(self.db[collection].find())

    def convert(self, data):
        return dict([(str(k), str(v)) for k, v in data.items()])
