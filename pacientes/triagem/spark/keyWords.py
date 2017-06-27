#!/usr/bin/env python

# Autor: Marcelo Paiva
# E_mail: marcelopaivaramos@gmail.com
# Data: 14/06/2017

# Importa bibliotecas utilizadas
from __future__ import print_function
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from kafka import KafkaClient, SimpleProducer, SimpleConsumer
import unicodedata
import re
from datetime import datetime

# Envia mensagens ao servidor kafka-broker
def putKafka(message):
    records = message.collect()
    if len(records) != 0:
        now = datetime.now()
        msg = "{\"datetime\":\"" + str(now.today()) + "\",\"keywords\":{\""
        t=1
        for record in records:
            if t:
                msg += str(record[0]) + "\":\"" + str(record[1])
                t=0
            else:
                msg += ",\"" + str(record[0]) + "\":\"" + str(record[1])
        msg += "\"}}"
        producer.send_messages(triTopic, msg)
    

# Filtro de caracteres
def lineFilter(line):
    newLine = unicodedata.normalize('NFKD', line.decode('utf-8')).encode('ASCII','ignore').strip()
    return re.sub('[^a-zA-Z0-9 \\\]', '', newLine)

# Programa principal
if __name__ == "__main__":

    # Help
    if len(sys.argv) != 5:
        print("Usage: kafka_wordcount.py <detServer> <detTopic> <triServer> <triTopic>", file=sys.stderr)
        exit(-1)

    # Armazena os argumentos nas respectivas variaveis
    detServer, detTopic, triServer, triTopic = sys.argv[1:]

    # Conecta ao servidor kafka-broker (spark -> kafka)
    kafkaServer = KafkaClient(triServer)
    producer = SimpleProducer(kafkaServer)
 
    # Conecta ao servidor kafka-zookeeper (spark <- kafka)
    sc = SparkContext(appName="PythonStreamingKafkaWordCount")
    ssc = StreamingContext(sc, 30)
    kvs = KafkaUtils.createStream(ssc, detServer, "spark-streaming-consumer", {detTopic: 1})
    lines = kvs.map(lambda x: x[1])
    counts = lines.flatMap(lambda line: line.split(" ")) \
        .filter(lambda word: "ebola" == word.lower() or "gripe" == word.lower() or "dor" == word.lower() or "londres" == word.lower()) \
        .map(lambda word: (lineFilter(word.lower()), 1)) \
        .reduceByKey(lambda a, b: a+b)
    counts.foreachRDD(putKafka)
    counts.pprint()

    ssc.start()
    ssc.awaitTermination()

