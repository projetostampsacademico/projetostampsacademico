from pymongo import MongoClient
from pprint import pprint
from bson.json_util import dumps

class MongoService:

    def __init__(self):
        client = MongoClient('mongodb://heroku_6c04n1s3:eg0rtjdqtmf8ukmmo3pfflqdbe@ds161630.mlab.com:61630/heroku_6c04n1s3')
        self.db = client.heroku_6c04n1s3

    def collection_names(self):
        return self.db.collection_names()

    def fetch_data(self, collection, format = 'json'):
        cursor = self.db[collection].find()
        if format == 'json':
            return dumps(cursor)
        else:
            return list(cursor)

    def query_data(self, collection, field, search, format = 'json'):
        cursor = self.db[collection].find({field : {'$regex' : ".*" + search + ".*"}})
        if format == 'json':
            return dumps(cursor)
        else:
            return list(cursor)

    def related_data(self, collection, collection_id, list, list_id):
        for item in list:
            if list_id in item:
                item['related'] = self.query_data(collection, collection_id, item[list_id], 'list')
        return list

    def find_all_in(self, collection, field, array, format = 'json'):
        cursor = self.db[collection].find({field : {"$in": array }})
        if format == 'json':
            return dumps(cursor)
        else:
            return list(cursor)

    def convert(self, data):
        return dict([(str(k), str(v)) for k, v in data.items()])
