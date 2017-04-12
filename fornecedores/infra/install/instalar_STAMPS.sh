#!/bin/bash

clear

apt-get install dialog

dialog --yesno 'Atualizar o Linux?' 5 40 
	 if [ $? = 0 ]; then 
		clear; 
		apt-get update
        	apt-get upgrade	 
	fi

dialog --yesno 'Instalar Standard system utilities?'  5 40 
	 if [ $? = 0 ]; then 
		clear;
        	apt-get install aptitude vim manpages dnsutils bsdmainutils psmisc python3-gdbm ufw dosfstools ed telnet powermgmt-base ntfs-3g ubuntu-release-upgrader-core iputils-tracepath groff-base bind9-host mtr-tiny bash-completion mlocate tcpdump geoip-database install-info irqbalance language-selector-common friendly-recovery command-not-found info hdparm man-db lshw update-manager-core apt-transport-https accountsservice command-not-found-data time ltrace parted popularity-contest strace ftp ubuntu-standard lsof glances  python-software-properties nodejs
	 fi

SERVER=$( dialog --stdout --title 'Qual Servidor'        \
        --menu '\nQual servidor esta instalando?\n\n'  \
        0 0 0                                    \
        API_WEB        'SERVIDOR 1 - API + WEB'  \
        BANCO_DADOS    'SERVIDOR 2 - BANCO DE DADOS' \

users=$( dialog --stdout --separate-output --title 'Criar Usuários'        \
   	--checklist '\nQuais Usuários deseja criar?\n\n'  \
   	0 0 0                                    \
   	1  'Time Scrum 01 - ts01'      off    \
	2  'Time Scrum 02 - ts02'      off    \
	3  'Time Scrum 03 - ts03'      off    \
	4  'Time Scrum 04 - ts04'      off    \

echo "$users" | while read USERID
do

	clear
	echo "##########################################"
	echo "##				        ##"
	echo "## Criando Conta do TIME 0$USERID             ##"
	echo "##                                      ##"
	echo "##########################################"

	USER="ts0$USERID"
	if grep -qs $USER /etc/passwd; then continue; fi

	useradd -s /bin/bash -m -d /home/$USER -c "SIG-TRAC - $USER"  -u 800$USERID  $USER

	sudo -u $USER mkdir /home/$USER/.ssh
	sudo -u $USER ssh-keygen -f /home/$USER/.ssh/key#$USER#$SERVER
	sudo -u $USER cat /home/$USER/.ssh/key#$USER#$SERVER.pub >> /home/$USER/.ssh/authorized_keys

	echo $USER >> .tmpUser


done


if [ $SERVER = "BANCO_DADOS" ];then

	ip=$(ifconfig | sed -n '/inet addr:/{p;q;}' | sed 's/ [^ ]\+ *$//g' | sed 's/ [^ ]\+ *$//g' | sed 's/^.*://')
  	clear
	echo "instalando Mysql"
	apt-get install mysql-server
	mysql_secure_installation
	sudo service mysql stop
	mv /etc/mysql/my.cnf /etc/mysql/my.cnf.old 
	cat /etc/mysql/my.cnf.old  | sed "s/127.0.0.1/$ip/g" > /etc/mysql/my.cnf
	sudo service mysql start

	clear
	echo "instalando MongoDB"
	aptitude install mongodb
	service mongodb stop
	cp /etc/mongodb.conf  /etc/mongodb.conf.old
	cat /etc/mongodb.conf.old | sed "s/127.0.0.1/$ip/g" > /etc/mongodb.conf
	service mongodb start
fi

if [ $SEVER = "API_WEB" ];then
	clear
	echo "instalando python"
	aptitude install python-software-properties python-setuptools
fi


if [ $SERVER = "PROCESSAMENTO" ];then
	clear
	echo "instalando Spark"
	aptitude install python-software-properties
	add-apt-repository ppa:webupd8team/java
	aptitude update
	aptitude install oracle-java8-installer oracle-java8-set-default
        echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment
        source /etc/environment
	cd /opt/
	wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.1-bin-hadoop2.6.tgz
	tar -xzvf spark-1.6.1-bin-hadoop2.6.tgz
	ln -s spark-1.6.1-bin-hadoop2.6  spark
	echo "SPARK_HOME=/opt/spark" >> /etc/environment
	echo 'PATH=$PATH:/opt/spark/bin/' >> /etc/environment
	source /etc/environment
fi 


