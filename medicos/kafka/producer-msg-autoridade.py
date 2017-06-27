# -*- coding: utf-8 -*-

from kafka import KafkaProducer
from datetime import datetime
import MySQLdb


__author__ = 'Victor Pugliese'


""""
    Para executar o script instale as seguintes dependências
      
    pip install kafka-python 
    sudo apt-get install python-mysqldb or pip install MySQL-python
    Se der algum problema entre em contato.

    victor.pugliese@outlook.com

    Observação: Esse código foi criado com ajuda do algoritimo
    desenvolvido por Samara Cardoso - samaracardosodossantos@gmail.com
    
"""    


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def conectDB():
    result = []
    
    try:
        conn = MySQLdb.connect(host="us-cdbr-iron-east-03.cleardb.net",
                     user="b6f15ede9bfc87",
                     passwd="5cad9d31",  
                     db="heroku_96fcc4c8ee9de87", 
                     port = 3306)
        
        cursor = conn.cursor()
        cursor.execute("""SELECT *
                         FROM mensagem WHERE msg_destinatario='authority'""")
        
        
        for linha in cursor.fetchall():
            result.append(dict_factory (cursor, linha))
        conn.close()
        
        if len(result) > 0:
            return result
        else:
            return ''
    
    except Exception as e:
        print 'Ocorreu na conexão com o banco de dados - '+ str(e)
        return ''

 
def prepareJson():
    list_screening = []
    screening = conectDB()
    
    if len(screening) > 0 :
        screening = conectDB()
    else:
        print 'Sem informações no Banco de Dados'
        return ''

    try:
        for i in range(0, len(screening)):
            data = {}
            data["id"] =  str(screening[i]['msg_id'])
            data["remetente"] =  str(screening[i]['msg_remetente'].encode('utf-8'))
            data["destinatario"] =  str(screening[i]['msg_destinatario'].encode('utf-8'))
            data["assunto"] =  str(screening[i]['msg_assunto'].encode('utf-8'))
            data["conteudo"] =  str(screening[i]['msg_conteudo'].encode('utf-8'))
            data["data"] =  str(screening[i]['msg_data'])
            data["criticidade"] =  str(screening[i]['msg_nivelCriticidade'])
            list_screening.append(data)
            
    except Exception as e:
        print 'Ocorreu na geração do JSON - '+ str(e)

    return list_screening

def sendMensage():
    
    infos_json = prepareJson()
    if len(infos_json) > 0:
        mensage = infos_json
    else:
        print 'Sem mensagens para ser enviada!'
        return ''
        

    try:
        producer = KafkaProducer(bootstrap_servers='34.204.88.242:9092')    
        for i in mensage:
            producer.send('msg-autoridade', str(i))
        
        print 'Mensagens envidas'
        
    except Exception as e:
        print 'Ocorreu um erro na envio da mensagem- '+ str(e)
        
    return 'Mensagem Enviada'

sendMensage()
