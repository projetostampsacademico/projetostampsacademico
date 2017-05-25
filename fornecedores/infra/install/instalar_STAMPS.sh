#!/bin/bash 

clear

apt-get install dialog

dialog --yesno 'Atualizar o Linux?' 5 40 
	 if [ $? = 0 ]; then 
		clear; 
		apt-get update
        	apt-get upgrade	 
	fi



dialog --yesno 'Instalar MYSQL utilizado em todos os servidores?'  5 40
         if [ $? = 0 ]; then
		clear
		echo "instalando Mysql"
        	apt-get install mysql-server
        	mysql_secure_installation
	 fi

dialog --yesno 'Instalar Standard system utilities?'  5 40 
	 if [ $? = 0 ]; then 
		clear;
        	apt-get install aptitude vim manpages dnsutils bsdmainutils psmisc ufw dosfstools ed telnet powermgmt-base ntfs-3g ubuntu-release-upgrader-core iputils-tracepath groff-base bind9-host mtr-tiny bash-completion mlocate tcpdump geoip-database install-info irqbalance language-selector-common friendly-recovery command-not-found info hdparm man-db lshw update-manager-core apt-transport-https accountsservice command-not-found-data time ltrace parted popularity-contest strace ftp ubuntu-standard lsof glances  python-software-properties nodejs rsync
	 fi

SERVER=$( dialog --stdout --title 'Qual Servidor'       \
        --menu '\nQual servidor esta instalando?\n\n'  	\
        0 0 0                                    	\
        API_WEB        'API + WEB'  			\
	PROCESSAMENTO  'PROCESSAMENTO' 			  )


if [[ $SERVER = "API_WEB" ]];then
	clear
	echo "instalando python"
	aptitude install python-software-properties python-setuptools python-pip
	pip install --upgrade pip
	pip install virtualenv
	
	echo "instalando LAMP"
	apt-get install apache2 
	apt-get install php libapache2-mod-php php-mcrypt php-mysql 

fi


if [[ $SERVER = "PROCESSAMENTO" ]];then
	clear
	echo "instalando Hadoop"
	aptitude install python-software-properties
	add-apt-repository ppa:webupd8team/java
	aptitude update
	aptitude install oracle-java8-installer oracle-java8-set-default
        echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment
        source /etc/environment
	useradd -d /usr/local/hadoop -m -s /bin/bash hadoop
	echo "Adicionar senha no Hadoop"
	passwd hadoop
	adduser hadoop sudo
	echo "Preparando HDFS"
        mkdir /hadoop
        chown hadoop:hadoop  /hadoop

	echo "Criando Chave"
	sudo -i -u hadoop ssh-keygen
	sudo -i -u hadoop ssh-copy-id hadoop@localhost
	echo "instalando Hadoop"
	sudo -i -u hadoop wget http://ftp.unicamp.br/pub/apache/hadoop/common/hadoop-2.8.0/hadoop-2.8.0.tar.gz
	sudo -i -u hadoop tar -xzf hadoop-2.8.0.tar.gz
	sudo -i -u hadoop ln -s /usr/local/hadoop/hadoop-2.8.0 /usr/local/hadoop/hadoop
	echo "HADOOP_HOME=/usr/local/hadoop/hadoop" >> 	/etc/environment
	echo "configurando Hadoop"
	chown hadoop:hadoop *.xml
	cp ./core-site.xml /usr/local/hadoop/hadoop/etc/hadoop/
        cp ./hdfs-site.xml /usr/local/hadoop/hadoop/etc/hadoop/
	echo "Formatando HDFS"
	sudo -i -u hadoop /usr/local/hadoop/hadoop/bin/hdfs namenode -format
	echo "configurando Yarn"
	cp ./mapred-site.xml /usr/local/hadoop/hadoop/etc/hadoop/
	cp ./yarn-site.xml  /usr/local/hadoop/hadoop/etc/hadoop/
	echo "instalando o hive"
	sudo -i -u hadoop wget http://ftp.unicamp.br/pub/apache/hive/hive-1.2.2/apache-hive-1.2.2-bin.tar.gz
	sudo -i -u hadoop tar -xzf apache-hive-1.2.2-bin.tar.gz
	sudo -i -u hadoop ln -s /usr/local/hadoop/apache-hive-1.2.2-bin /usr/local/hadoop/hive
	echo "HIVE_HOME=/usr/local/hadoop/hive" >>  /etc/environment

	echo "configurando metastore"
	apt-get install libmysql-java
	sudo -i -u hadoop ln -s /usr/share/java/mysql-connector-java.jar /usr/local/hadoop/hive/lib/mysql-connector-java.jar
	cd /usr/local/hadoop/hive/scripts/metastore/upgrade/mysql
	
	echo "Criando Databases - Entre com a senha do Mysql"
	mysql -u root -p  -e "CREATE DATABASE metastore CHARACTER SET utf8 COLLATE utf8_general_ci";
	mysql -u root -p metastore < hive-schema-0.14.0.mysql.sql

	mysql -u root -p -e " CREATE USER 'hiveuser'@'localhost' IDENTIFIED BY 'hivepassword';"
	mysql -u root -p -e " GRANT all on metastore.* to 'hiveuser'@'localhost' identified by 'hivepassword';"
	mysql -u root -p -e " flush privileges"

	cd
	cp ./hive-site.xml /usr/local/hadoop/hive/conf
	
	echo "start HDFS + YARN"
	sudo -i -u hadoop /usr/local/hadoop/hadoop/sbin/start-dfs.sh 
	sudo -i -u hadoop /usr/local/hadoop/hadoop/sbin/start-yarn.sh

	echo "Testando HDFS"
	sudo -i -u hadoop /usr/local/hadoop/hadoop/bin/hdfs dfs -mkdir       /tmp
	sudo -i -u hadoop /usr/local/hadoop/hadoop/bin/hdfs dfs -mkdir       /user
	sudo -i -u hadoop /usr/local/hadoop/hadoop/bin/hdfs dfs -mkdir	     /user/hive/
        sudo -i -u hadoop /usr/local/hadoop/hadoop/bin/hdfs dfs -mkdir       /user/hive/warehouse
	sudo -i -u hadoop /usr/local/hadoop/hadoop/bin/hdfs dfs -chmod g+w   /tmp
	sudo -i -u hadoop /usr/local/hadoop/hadoop/bin/hdfs dfs -chmod g+w   /user/hive/warehouse
 			
fi 


