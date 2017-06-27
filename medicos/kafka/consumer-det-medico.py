# -*- coding: utf-8 -*-

from kafka import KafkaConsumer

__author__ = 'Samara Cardoso'

""""
    Para executar o script instale as seguintes dependência
      
    pip install kafka-python
    
    Se der algum problema entre em contato comigo
    samaracardosodossantos@gmail.com
    
"""

consumer = KafkaConsumer(bootstrap_servers='34.204.88.242:9092',
                                 auto_offset_reset='earliest')


consumer.subscribe(['det-medico'])
for message in consumer:
    print (message.value)


