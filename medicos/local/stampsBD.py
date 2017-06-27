__author__ = 'fkfouri'

from pymongo import MongoClient
_conn = "mongodb://heroku_6c04n1s3:eg0rtjdqtmf8ukmmo3pfflqdbe@ds161630.mlab.com:61630/heroku_6c04n1s3"


def DB_TEST():
    ''' TESTE DE CONEXAO '''
    client = MongoClient(_conn)
    print(client.server_info())


def START_CONN():
    ''' DOC STRING '''
    client = MongoClient(_conn)
    db = client.get_default_database()
    # print client.server_info()
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


def GET_CID_10_SUBCATEGORIAS():
    '''busca por dados da tabela CID_10_SUCBATEGORIAS'''
    db = START_CONN()
    collection = db['CID-10-SUBCATEGORIAS'].find({})
    i, lst = 0, []
    for document in collection:

        CID_STAMPS = document['SUBCAT']
        tst = CID_STAMPS[1:-1]
        tst2 = CID_STAMPS[:1]

        if CID_STAMPS[:1] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']:
            lst.append(document)
        elif CID_STAMPS[:1] == 'N' and int(CID_STAMPS[1:-1]) > 7:
            lst.append(document)

        i += 1
        '''
        lst.append(document)
        i += 1
        '''
        # if i>10:
        #    break
    return lst


def GET_DETAIL(info):
    '''Evita duplicidades na base de details'''
    db = START_CONN()
    ref = db['DETAIL']
    return ref.find_one({"info": info})


def UPDATE_DETAIL(_id, CID_STAMPS, ICD):
    ''' doc string'''
    db = START_CONN()
    ref = db['DETAIL']
    ref.update_one({"_id" : _id}, {'$set': {'CID_STAMPS': CID_STAMPS, 'ICD': ICD}})


def GET_DETAIL_UNTRANSLATED():
    '''Obtem todos os registros da tabela Detail ainda nao traduzido'''
    db = START_CONN()
    ref = db['DETAIL']
    return ref.find({"Info_PT" : None })


def UPDATE_DETAIL_TRANSLATE(_id, info_PT, symptoms_PT):
    ''' doc string'''
    db = START_CONN()
    ref = db['DETAIL']
    ref.update_one({"_id" : _id}, {'$set': {'info_PT': info_PT, 'symptoms_PT': symptoms_PT}})


# GET_CID_10_SUBCATEGORIAS()
'''
db = START_CONN()
ref = db['CID-10-SUBCATEGORIAS']


ref = GET_CID_10_SUBCATEGORIAS()
print(ref)
'''
#DB_TEST()

