from pymongo import MongoClient
from pprint import pprint
from bson.json_util import dumps
from nosql.util import Util

class MongoService:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
            client = MongoClient('mongodb://heroku_6c04n1s3:eg0rtjdqtmf8ukmmo3pfflqdbe@ds161630.mlab.com:61630/heroku_6c04n1s3')
            cls.instance.db = client.heroku_6c04n1s3
        return cls.instance

    def collection_names(self):
        return self.db.collection_names()

    def fetch_data(self, collection, format = 'json'):
        cursor = self.db[collection].find()
        if format == 'json':
            return dumps(cursor)
        else:
            return list(cursor)

    def fetch_unique_list(self, collection, field):
        cursor = self.db[collection].find(projection={'symptoms': True, '_id': False})
        array_json_with_lists = list(cursor)
        field_list = [symptom for json in array_json_with_lists for symptom in json[field]]
        return Util().unique(field_list)

    def query_data(self, collection, field, search, format = 'json'):
        cursor = self.db[collection].find({field : {'$regex' : ".*" + search + ".*"}})
        if format == 'json':
            return dumps(cursor)
        else:
            return list(cursor)

    def related_data(self, collection, collection_id, field, list, list_id='code'):
        for item in list:
            if list_id in item:
                item[field] = self.query_data(collection, collection_id, item[list_id], 'list')
        return list

    def find_all_in(self, collection, field, array, format = 'json'):
        cursor = self.db[collection].find({field : {"$in": array }})
        if format == 'json':
            return dumps(cursor)
        else:
            return list(cursor)

    def convert(self, data):
        return dict([(str(k), str(v)) for k, v in data.items()])
