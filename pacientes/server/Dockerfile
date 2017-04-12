FROM node:6

MAINTAINER Luiz Coura <luizcoura@gmail.com>

ENV DB mongodb://mongodb/pacientes 

ADD . /var/www/pacientes
WORKDIR /var/www/pacientes

RUN npm install \
 && npm install -g bower \
 && bower install --allow-root

EXPOSE 3000

CMD ["npm", "start"]

