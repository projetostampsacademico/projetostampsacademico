FROM node:6

MAINTAINER Luiz Coura <luizcoura@gmail.com>

ADD . /var/www/timeline
WORKDIR /var/www/timeline

RUN npm install \
 && npm install -g bower \
 && bower install --allow-root

EXPOSE 8080

CMD ["npm", "start"]

