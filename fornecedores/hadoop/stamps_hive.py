#!./env/bin/python2.7
import thrift_sasl
from pyhive import hive
from kafka import KafkaProducer, KafkaConsumer
from datetime import datetime
from pprint import pprint
import json
import time
import threading


class consulta_hive(threading.Thread):
    def __init__(self, argumento):
        threading.Thread.__init__(self)
        self.argumento = argumento

    def run(self):
        cursor = hive.Connection(host='192.168.56.101', port=10000, username='hadoop', database='fornecedores').cursor()
        query = "select movimentacao.des_estado, movimentacao.des_cidade, movimentacao.medicamento, sum(movimentacao.quantidade) as quantidade \
                         from movimentacao where  movimentacao.medicamento = "+self.argumento+" GROUP BY movimentacao.des_estado, movimentacao.des_cidade, movimentacao.medicamento"
        # query = "select movimentacao.des_estado, movimentacao.des_cidade, movimentacao.medicamento from movimentacao where  movimentacao.medicamento = 'ZIRVIT MULTI 30 CP A ARESE' "
        print(query)
        cursor.execute(query)
        for i in cursor.fetchall():
            print(i)
            msg = {'keywords': {'quantidade': i[3], 'produto': i[2], 'local': i[1] + '-' + i[0]}, 'datatime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            producer = KafkaProducer(bootstrap_servers='192.168.56.101:9093', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
            producer.send('test-result', msg)
            producer.flush()
            print(msg)


lock = threading.Lock()
threads = []
#hive_conect = pyhs2.connect(host='192.168.56.101', port=10000, authMechanism="PLAIN", user='hadoop', password='mcosta', database='fornecedores')
consumer = KafkaConsumer('test-insert', group_id='my-group', bootstrap_servers=['192.168.56.101:9093'], enable_auto_commit=True)
for message in consumer:
    medicamento = message.value
    print (medicamento)
    thread_hive = consulta_hive(medicamento)
    thread_hive.start()
    threads.append(thread_hive)

