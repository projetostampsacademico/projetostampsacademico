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

	# convert numero em data - 
	_date = datetime.fromtimestamp(time.mktime(time.localtime(x.symptomsdate)))
	
	try:
		conn = getConnMySQL()

		query = ("INSERT INTO tri_paciente (email, user_name, latitude, longitude, date_register, symptoms, offset) " \
				"VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')").format(x.email, x.username, float(x.latitude), float(x.longitude), _date, _symptoms, int(_offset))


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


