# pacientes

Para desenvolver:
```bash
docker-compose build
docker-compose run -p 8080:3000 server bash
```

Para colocar em produção:
```bash
docker-compose build
docker-compose up -d
docker-compose logs -f server
```
