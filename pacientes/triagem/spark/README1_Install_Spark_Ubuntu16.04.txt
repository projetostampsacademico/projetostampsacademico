Autor: Marcelo Paiva
E_mail: marcelopaivaramos@gmail.com
Data: 30/05/2017

- Manual de instalação do Spark - Ubuntu 16.04
==============================================================

// IP
Spark:  192.168.0.101

// Atualizar sistema operacional e instalar dependências: java e scala
$ sudo aptitude update
$ sudo aptitude upgrade
$ sudo aptitude install openjdk-8-jdk scala
$ sudo update-java-alternatives -s java-1.8.0-openjdk-amd64

$ java -version
openjdk version "1.8.0_131"
OpenJDK Runtime Environment (build 1.8.0_131-8u131-b11-0ubuntu1.16.04.2-b11)
OpenJDK 64-Bit Server VM (build 25.131-b11, mixed mode)

$ scala -version
Scala code runner version 2.11.6 -- Copyright 2002-2013, LAMP/EPFL

// Instalar o spark v.2.1.1
$ wget https://d3kbcqa49mib13.cloudfront.net/spark-2.1.1-bin-hadoop2.7.tgz
$ sudo tar xvf spark-2.1.1-bin-hadoop2.7.tgz
$ sudo mv spark-2.1.1-bin-hadoop2.7 /usr/local/spark
$ sudo chown -R root:root /usr/local/spark
$ sudo vim /etc/environment
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/spark/bin"
$ export PATH="$PATH:/usr/local/spark/bin"

// Instalar pacote para integração com kafka
$ sudo aptitude install python-kafka

// Alterar configuração do log para diminuir mensagens na tela
$ cd /usr/local/spark/conf
$ sudo cp log4j.properties.template log4j.properties
$ sudo vim log4j.properties
De: log4j.rootCategory=INFO, console
Para: log4j.rootCategory=ERROR, console

// Teste
$ spark-shell
$ pyspark

