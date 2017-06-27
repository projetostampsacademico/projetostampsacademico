__author__ = 'fkfouri'

import sys
import csv
import stampsBD as bd
import json
from unidecode import unidecode
import os


def READ_FILE(_file, _table):
    ''' Faz a leitura do arquivo e envia para o Banco'''

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
                    if len(field)> 0: 
                        idx = header.index(field)
                        row[idx]=item[idx]
                        #j[field]=item[idx]
                        j[field]=unidecode(item[idx])
                
                lst.append(j)
                #jj = json.loads(json.dumps(j, separators=(',',':')))
                #st.INSERT_MONGO('CAPITULOS', jj)

        SEED_DATA = json.loads(json.dumps(lst, separators=(',',':')))
        bd.BULK_INSERT_MONGO(_table, SEED_DATA)
        #data = bson.BSON.encode(SEED_DATA)


myPath = sys.path[0] + str('\CID')
for x in os.walk(myPath):
    corrente = x[0]
    diretorios = x[1]
    arquivos = x[2]
    '''
    print("Corrente: " + corrente)
    print("Diretorios: " + str(diretorios))
    print("Arquivos: ")
    print(arquivos)
    '''

    for arquivo in arquivos:
        if arquivo.upper().endswith('.CSV'):
            tableName = str(arquivo.upper().replace('.CSV',''))
            _fileAddress = str(corrente) + str("/") + str(arquivo)
            print ('======> ' + _fileAddress)
            READ_FILE(_fileAddress, tableName)


