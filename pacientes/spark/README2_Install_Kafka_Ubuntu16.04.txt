Autor: Marcelo Paiva
E_mail: marcelopaivaramos@gmail.com
Data: 30/05/2017

- Manual de instalação do Kafka - Ubuntu 16.04
==============================================================

IP:
Kafka:  192.168.0.102

// Atualizar sistema operacional e instalar dependência: java
$ sudo aptitude update
$ sudo aptitude upgrade
$ sudo aptitude install openjdk-8-jdk
$ sudo update-java-alternatives -s java-1.8.0-openjdk-amd64

$ java -version
openjdk version "1.8.0_131"
OpenJDK Runtime Environment (build 1.8.0_131-8u131-b11-0ubuntu1.16.04.2-b11)
OpenJDK 64-Bit Server VM (build 25.131-b11, mixed mode)

// Instalar o kafka v.2.11
$ sudo wget http://ftp.unicamp.br/pub/apache/kafka/0.10.2.0/kafka_2.11-0.10.2.0.tgz
$ sudo tar xzvf kafka_2.11-0.10.2.0.tgz
$ sudo mv kafka_2.11-0.10.2.0 /usr/local/kafka
$ sudo chown -R root:root /usr/local/kafka
$ sudo vim /etc/environment
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/kafka/bin"
$ export PATH="$PATH:/usr/local/kafka/bin"

// Inicializar o zookeeper e kafka broker
$ sudo zookeeper-server-start.sh /usr/local/kafka/config/zookeeper.properties &
$ sudo kafka-server-start.sh /usr/local/kafka/config/server.properties &

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

// Teste
- Terminal 1 (Kafka - consumer)
$ sudo kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

- Terminal 2 (Kafka - producer)
$ sudo kafka-console-producer.sh --broker-list localhost:9092 --topic test
Ola Mundo!!! <Enter>

- Terminal 1 (Kafka - consumer)
Ola Mundo!!!

