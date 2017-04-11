# pacientes
Segmento Pacientes

Para desenvolver:
docker-compose build
docker-compose run -p 8080:3000 server bash

Para colocar em produção:
docker-compose build
docker-compose up -d
docker-compose logs -f server
