# -*- coding: cp1252 -*-
import MySQLdb

__author__ = 'Victor Pugliese'

""""
    Responsavel pela leitura e armazenamento dos dados do Kafta-tri-paciente
"""

def getConnMySQL():
	conn = MySQLdb.connect(	host="us-cdbr-iron-east-03.cleardb.net", 
				   		user="b6f15ede9bfc87",
						passwd="5cad9d31",  
						db="heroku_96fcc4c8ee9de87", 
						port = 3306)

	return conn

def SaveRecord():
	
	try:
		conn = getConnMySQL()

		query = ("CALL proc_Ebola();")

		#print(query)

		cursor = conn.cursor()
		cursor.execute(query)
		conn.commit()

		####

                query = ("CALL proc_RequisitarMedicamento();")

		#print(query)

		cursor = conn.cursor()
		cursor.execute(query)
		conn.commit()
                
	except Exception as e:

		print 'Erro na conexão com o banco de dados MySQL - '+ str(e)

	finally:
		cursor.close()
		conn.close()

SaveRecord()
