# -*- coding: utf-8 -*-

from kafka import KafkaProducer
from datetime import datetime
import MySQLdb


__author__ = 'Samara Cardoso'


""""
    Para executar o script instale as seguintes dependências
      
    pip install kafka-python 
    sudo apt-get install python-mysqldb or pip install MySQL-python

    Se der algum problema entre em contato comigo
    samaracardosodossantos@gmail.com
    
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
        cursor.execute("""SELECT con_entry_time, con_doctor_crm_id, con_hospital_id_id, con_patient_number_id, con_triagem_id_id,
                                con_diagnostico, con_evolucao, con_prescricao, con_tratamento, tri_pressao, tri_temperatura,
                                tri_diabete, tri_problem, tri_manchester, tri_enfermeiro_id
                         FROM consulta, triagem
                         WHERE con_triagem_id_id = triagem.id""")
        
        
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
    
    if len(conectDB()) > 0 :
        screening = conectDB()
    else:
        print 'Sem informações no Banco de Dados'
        return ''

    try:
        for i in range(0, len(screening)):
            data = {}
            data["resourceType"] = "ClinicalImpression"
            data["identifier"] =  [1,20]
            data["status"]  = "In Progress"
            data["code"]  = str(i)
            data["description"] =  str(screening[i]['con_diagnostico'].encode('utf-8')) 
            data["subject"] =  { str(screening[i]['con_patient_number_id']) } 
            data["context"] =  { str(screening[i]['con_patient_number_id']) }
            data["date"] =  str(datetime.now())
            data["assessor"] =  { str(screening[i]['con_doctor_crm_id'])}
            data["summary"] =  ""
            data["prognosisCodeableConcept"] =  []
            data["prognosisReference"] =  []
            data["note"] =  []
            
            list_screening.append(data)
            
    except Exception as e:
        print 'Ocorreu na geração do JSON - '+ str(e)

    return list_screening



def sendMensage():
    
    if len(prepareJson()) > 0:
        mensage = prepareJson()
    else:
        print 'Sem mensagens para ser enviada!'
        return ''
        

    try:
        producer = KafkaProducer(bootstrap_servers='34.204.88.242:9092')    
        for i in mensage:
            producer.send('det-medico', str(i))
        
        print 'Mensagens enviadas'
        
    except Exception as e:
        print 'Ocorreu um erro na envio da mensagem- '+ str(e)
        
    return 'Mensagem Enviada'

sendMensage()