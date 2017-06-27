#!./env/bin/python2.7
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pprint import pprint
from kafka import KafkaProducer
from datetime import datetime
import time
import pymysql.cursors
import json



#chaves de app do Twitter 
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret =

poll_interval = 5

#conecao com o Mysql
connection = pymysql.connect(host='localhost', port=3306, user='root', password='123456',db='busca',
                             cursorclass=pymysql.cursors.DictCursor,charset='utf8mb4',autocommit=True
                             )
cursor = connection.cursor()

#Classe hedada do Tweepy
class StdOutListener(StreamListener):
    def on_data(self, data):
        twit = json.loads(data)
	# configuracao kafka
        producer = KafkaProducer(bootstrap_servers='192.168.56.101:9093', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        producer.send('test2', {'msg': twit["text"], 'datatime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        producer.flush()
        print(twit["text"])
        return True

    def on_error(self, status):
        if status == 420:
            return False

#Busca palavras no Mysql
def get_keywords_fromdb():
    cursor.execute("select palavra from palavras where ativa = 1;");
    keywords = [item['palavra'] for item in cursor.fetchall()]
    return keywords

#Busca locais no Mysql
def get_locations_fromdb():
    locationBD =[]
    cursor.execute("select lat1,lon1,lat2,lon2 from locais where ativa = 1;");
    for item in cursor.fetchall():
        locationBD.append(float(item['lat1']))
        locationBD.append(float(item['lon1']))
        locationBD.append(float(item['lat2']))
        locationBD.append(float(item['lon2']))
    return locationBD

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth,StdOutListener())
    keywords = get_keywords_fromdb()
    locationBD = get_locations_fromdb()
    while True:
        if stream.running is True:
            stream.disconnect()
            time.sleep(3)
            keywords = get_keywords_fromdb()
            locationBD = get_locations_fromdb()

            print("***************************************************")
            pprint(keywords)
            pprint(locationBD)

            if keywords.__len__() == 0:
                stream.disconnect()
                break

        stream.filter(track=keywords,locations=locationBD,async=True)
        time.sleep(10)
