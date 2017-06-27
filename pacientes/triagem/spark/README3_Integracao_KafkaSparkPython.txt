Autor: Marcelo Paiva
E_mail: marcelopaivaramos@gmail.com
Data: 30/05/2017

- Integração:  Kafka, Spark e Python
==============================================================

IPs:
Spark:  192.168.0.101
Kafka:  192.168.0.102

// Baixar o .jar para integração
http://spark.apache.org/docs/latest/streaming-kafka-0-8-integration.html
Download:  spark-streaming-kafka-0-8-assembly_2.11-2.1.1.jar

// Instalar pacote para integração com kafka
$ sudo aptitude install python-kafka

// Teste - Contar palavras
- Terminal 1 (Spark)
$ sudo spark-submit --jars /home2/paiva/spark-streaming-kafka-0-8-assembly_2.11-2.1.1.jar examples/src/main/python/streaming/kafka_wordcount.py 192.168.0.102:2181 test

- Terminal 2 (Kafka - producer)
Ola Mundo!!! <Enter>

- Terminal 3 (Kafka - consumer)
Ola Mundo!!!

- Terminal 1 (Spark)
-------------------------------------------
Time: 2017-05-24 19:05:22
-------------------------------------------
(u'Ola', 1)
(u'Mundo!!!', 1)

- Terminal 2 (Kafka - producer)
Testando palavras repetidas: teste oi teste oi teste oi <Enter>

- Terminal 3 (Kafka - consumer)
Testando palavras repetidas: teste oi teste oi teste oi

- Terminal 1 (Spark)
-------------------------------------------
Time: 2017-05-24 19:40:47
-------------------------------------------
(u'palavras', 1)
(u'teste', 3)
(u'Testando', 1)
(u'oi', 3)
(u'repetidas:', 1)

