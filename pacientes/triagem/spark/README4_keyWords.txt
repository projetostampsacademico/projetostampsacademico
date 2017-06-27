Autor: Marcelo Paiva
E_mail: marcelopaivaramos@gmail.com
Data: 30/05/2017

- Manual do usuário:  TS01-US213
==============================================================

// Criar os tópicos "test", "det-twitter", "tri-twitter" e verificar se os mesmos foram criado
$ sudo kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
$ sudo kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic det-twitter
$ sudo kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic tri-twitter
$ sudo kafka-topics.sh --list --zookeeper localhost:2181
__consumer_offsets
det-twitter
first
test
tri-twitter

// Testar os tópicos "det-twitter" e "tri-twitter"
- Terminal 1 (kafka - consumer)
$ sudo kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic det-twitter --from-beginning

- Terminal 2 (kafka - consumer)
$ sudo kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic tri-twitter --from-beginning

- Terminal 3 (kafkacat)
$ echo "Testando topico det-twitter" | kafkacat -P -b 34.204.88.242:9092 -t det-twitter
$ echo "Testando topico tri-twitter" | kafkacat -P -b 34.204.88.242:9092 -t tri-twitter

- Terminal 1 (kafka - consumer)
Testando topico det-twitter
OK!

- Terminal 2 (kafka - consumer)
Testando topico tri-twitter
OK!


// Testar TS01-US213 - integração: Kafka, Spark e Python
- Terminal 1 (kafka - consumer)
$ sudo kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic det-twitter --from-beginning
ou
$ sudo kafka-console-consumer.sh --bootstrap-server localhost:443 --topic det-twitter --from-beginning

- Terminal 2 (kafka - consumer)
$ sudo kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
ou
$ sudo kafka-console-consumer.sh --bootstrap-server localhost:443 --topic test --from-beginning

- Terminal 4 (spark server)
$ spark-submit --jars /home2/paiva/spark-streaming-kafka-0-8-assembly_2.11-2.1.1.jar keyWords.py 34.204.88.242:2181 det-twitter 34.204.88.242:9092 test
ou
$ spark-submit --jars /home2/paiva/spark-streaming-kafka-0-8-assembly_2.11-2.1.1.jar keyWords.py 34.204.88.242:80 det-twitter 34.204.88.242:443 test

- Terminal 3 (kafkacat)
$ echo "teste Teste TESTE ebola Ebola EBOLA eBOLA" | kafkacat -P -b 34.204.88.242:9092 -t det-twitter
ou
$ echo "teste Teste TESTE ebola Ebola EBOLA eBOLA" | kafkacat -P -b 34.204.88.242:443 -t det-twitter

- Terminal 1 (kafka - consumer)
teste Teste TESTE ebola Ebola EBOLA eBOLA

- Terminal 4 (spark server)
-------------------------------------------
Time: 2017-05-30 19:42:26
-------------------------------------------
(u'teste', 3)
(u'ebola', 4)

- Terminal 2 (kafka - consumer)
{"datetime":"2017-05-30 19:42:26.392062","keywords":{"teste":"3,"ebola":"4"}}

