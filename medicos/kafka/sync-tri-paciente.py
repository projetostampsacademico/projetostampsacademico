# -*- coding: utf-8 -*-

from kafka import KafkaConsumer
from datetime import datetime
import time
import MySQLdb
import json
from collections import namedtuple


__author__ = 'Fabio Kfouri/Victor Pugliese'

""""
    Responsavel pela leitura e armazenamento dos dados do Kafta-tri-paciente
"""

def generate_ebola_diagnosis(patientSymptomsList):
    #ebolaSymptomsList = ["Fever", "Headache", "Joint and muscle aches", "Weakness", "Diarrhea", "Vomiting", "Stomach pain", "Lack of appetite"]
    search_regex = "|".join(patientSymptomsList)
    EBOLA_THRESHOLD = 0.8
    ebolaSymptomsParameters = dict()
    ebolaSymptomsParameters['Fever'] = 0.06
    ebolaSymptomsParameters['Headache'] = 0.04
    ebolaSymptomsParameters['Joint and muscle aches'] = 0.25
    ebolaSymptomsParameters['Weakness'] = 0.05
    ebolaSymptomsParameters['Diarrhea'] = 0.15
    ebolaSymptomsParameters['Vomiting'] = 0.15
    ebolaSymptomsParameters['Stomach pain'] = 0.15
    ebolaSymptomsParameters['Lack of appetite'] = 0.15
    probability = 0.0
    for patientSymptom in patientSymptomsList:
        if patientSymptom in ebolaSymptomsParameters:
            probability = probability + ebolaSymptomsParameters[patientSymptom]
    print (probability)
    if probability >= EBOLA_THRESHOLD:
        return 'a984'
    return ''


''' Retorna a conexao com o MySQL '''
def getConnMySQL():
	conn = MySQLdb.connect(	host="us-cdbr-iron-east-03.cleardb.net", 
				   		user="b6f15ede9bfc87",
						passwd="5cad9d31",  
						db="heroku_96fcc4c8ee9de87", 
						port = 3306)

	return conn

''' Limpa a base '''
def clearTable():
	conn = getConnMySQL()
	cursor = conn.cursor()
	query = "TRUNCATE TABLE tri_paciente"
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()


''' Responsavel por salvar os dados no Banco '''
def SaveRecord(_record):
	#transforma json em objeto
	x = json.loads(_record.value, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
	_offset = _record.offset

	#transforma e limpa um array de sintomas em string separado por ponto e virgula
	_symptoms = '; '.join(str(e).replace('-','').strip() for e in x.symptoms)

        #verifica incidencia ebola
        ebola = generate_ebola_diagnosis(x.symptoms)
        	
	# convert numero em data - 
	_date = datetime.fromtimestamp(time.mktime(time.localtime(x.symptomsdate)))
	
	try:
		conn = getConnMySQL()

		query = ("INSERT INTO tri_paciente (email, user_name, latitude, longitude, date_register, symptoms, disease, offset) " \
				"VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')").format(x.email, x.username, float(x.latitude), float(x.longitude), _date, _symptoms, ebola, int(_offset))


		#print(query)

		cursor = conn.cursor()
		cursor.execute(query)
		conn.commit()

	except Exception as e:

		print 'Erro na conexão com o banco de dados MySQL - '+ str(e)

	finally:
		cursor.close()
		conn.close()
		
''' Consome os dados do Kafta '''		
def consumeKafta():
	consumer = KafkaConsumer(bootstrap_servers='34.204.88.242:9092',
	                                 auto_offset_reset='earliest')


	consumer.subscribe(['tri-paciente'])
	for message in consumer:
	    SaveRecord(message)
	    #print (message)


clearTable()
consumeKafta()


