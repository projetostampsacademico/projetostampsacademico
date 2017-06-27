__author__ = 'fkfouri'

import sys
import json
import stampsBD as bd

def READ_FILE(_file):
    ''' Faz a leitura do arquivo e envia para o Banco'''

    print(_file)

    group = ''
    lstGroup, lstSubGroup = [], []

    with open(_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for item in lines:
            idx = item[1-1:6-1].strip()
            code = item[7-1:14-1].strip()
            tipo = item[15-1:16-1].strip()
            desc = item[78-1:-1].strip()

            if tipo=='0':
                seed = {}
                seed['code'] = code
                seed['description'] = desc
                seed['search'] = code + ' ' + desc

                group = code
                lstGroup.append(seed)

                # seed_data = json.loads(json.dumps(seed, separators=(',', ':')))
                # bd.INSERT_MONGO('Category', seed_data)

            else:
                seed = {}
                seed['code'] = code
                seed['description'] = desc
                seed['group'] = group
                seed['search'] = code + ' ' + desc
                lstSubGroup.append(seed)

                # seed_data = json.loads(json.dumps(seed, separators=(',', ':')))
                # bd.INSERT_MONGO('SubCategory', seed_data)

    seed_Group = json.loads(json.dumps(lstGroup, separators=(',', ':')))
    bd.BULK_INSERT_MONGO('Category', seed_Group)

    seed_SubGroup = json.loads(json.dumps(lstSubGroup, separators=(',', ':')))
    bd.BULK_INSERT_MONGO('SubCategory', seed_SubGroup)

    t= 1

    '''
    with open(_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        myList = list(reader)

        header, lst, row = [], [], {}

        for item in myList:

            if header == []:
                header = item
            else:
                j = {}
                for field in header:
                    if len(field) > 0:
                        idx = header.index(field)
                        row[idx] = item[idx]
                        # j[field]=item[idx]
                        j[field] = unidecode(item[idx])

                lst.append(j)
                # jj = json.loads(json.dumps(j, separators=(',',':')))
                # st.INSERT_MONGO('CAPITULOS', jj)

        SEED_DATA = json.loads(json.dumps(lst, separators=(',', ':')))
        bd.BULK_INSERT_MONGO(_table, SEED_DATA)
        # data = bson.BSON.encode(SEED_DATA)          
    
    '''



myPath = sys.path[0] + str('/CID/')
file = myPath + 'icd10cm_order_2017.txt'
READ_FILE(file)