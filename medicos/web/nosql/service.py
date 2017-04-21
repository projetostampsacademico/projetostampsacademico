from pymongo import MongoClient


class MongoService:

    def __init__(self):
        client = MongoClient('mongodb://heroku_6c04n1s3:eg0rtjdqtmf8ukmmo3pfflqdbe@ds161630.mlab.com:61630/heroku_6c04n1s3')
        self.db = client.heroku_6c04n1s3

    def collection_names(self):
        self.db.collection_names()

    def fetch_data(self):
        [doc for doc in self.db.stamps.find()]
