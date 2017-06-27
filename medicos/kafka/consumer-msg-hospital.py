# -*- coding: utf-8 -*-

from kafka import KafkaConsumer

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
consumer = KafkaConsumer(bootstrap_servers='34.204.88.242:9092',
                                 auto_offset_reset='earliest')


consumer.subscribe(['msg-hospital'])
for message in consumer:
    print (message.value)
