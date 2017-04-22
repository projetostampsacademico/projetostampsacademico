__author__ = 'fkfouri'

from pymongo import MongoClient

def START_CONN():
    ''' DOC STRING '''

    conn = "mongodb://heroku_6c04n1s3:eg0rtjdqtmf8ukmmo3pfflqdbe@ds161630.mlab.com:61630/heroku_6c04n1s3"
    client = MongoClient(conn)
    db = client.get_default_database()
    #print client.server_info()
    return db 

def INSERT_MONGO(table, seed):
    ''' doc string'''
    db = START_CONN()
    ref = db[table]
    ref.insert_one(seed)
    

def BULK_INSERT_MONGO(table, seed):
    ''' Insercao do tipo Bulk'''
    db = START_CONN()
    ref = db[table]
    ref.insert_many(seed)
    