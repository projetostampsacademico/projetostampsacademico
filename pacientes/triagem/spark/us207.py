#!/usr/bin/env python

# Autor: Marcelo Paiva
# E_mail: marcelopaivaramos@gmail.com
# Data: 30/05/2017

# Importa bibliotecas utilizadas
from __future__ import print_function
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from kafka import KafkaClient, SimpleProducer, SimpleConsumer

# Envia mensagens ao servidor kafka-broker
def putKafka(message):
    records = message.collect()
    for record in records:
        producer.send_messages(triTopic, str(record))

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
    ssc = StreamingContext(sc, 1)
    kvs = KafkaUtils.createStream(ssc, detServer, "spark-streaming-consumer", {detTopic: 1})
    lines = kvs.map(lambda x: x[1])
    #counts = lines
    counts = lines.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a+b)
    counts.foreachRDD(putKafka)
    counts.pprint()

    ssc.start()
    ssc.awaitTermination()

