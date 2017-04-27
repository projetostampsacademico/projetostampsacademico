FROM node:6

MAINTAINER Luiz Coura <luizcoura@gmail.com>

ENV IP mongodb
ENV COMPOSER_ALLOW_SUPERUSER 1 

ADD . /var/www/pacientes
WORKDIR /var/www/pacientes

RUN npm install \
 && npm install -g bower \
 && bower install --allow-root

EXPOSE 8080

CMD ["npm", "start"]

