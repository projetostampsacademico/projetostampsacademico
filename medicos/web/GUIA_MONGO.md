Projeto STAMPS - TS#02 Segmento Médico
=======================================

Para ir além, depois de instalado: [Tutorial](http://django-mongodb-engine.readthedocs.io/en/latest/tutorial.html)

Guia do Mongodb
---------------

1. Faça o download do Mongodb (Comunity Server)[download](https://www.mongodb.com/download-center?jmp=nav)


2. Instale o Mongodb [instalar no windows](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)

  Basicamente, entrar na pasta de instalação do mongodb, definir o seu diretório de dados:

  ```bash
  "C:\Program Files\MongoDB\Server\3.4\bin\mongod.exe" --dbpath d:\stamps
  ```
  Em outro terminal, começar o mongodb:

  ```bash
  "C:\Program Files\MongoDB\Server\3.4\bin\mongod.exe"
  ```
  Conectar-se no mongodb e executar os comandos o item 3:

  ```bash
  "C:\Program Files\MongoDB\Server\3.4\bin\mongo.exe
  ```

3. Crie um novo banco de dados [banco de dados](https://www.tutorialspoint.com/mongodb/mongodb_create_database.htm)

  Resumidamente, criar o banco de dados:

  ```bash
  use STAMPS_DB
  ```

4. Baixar o repositório https://github.com/django-nonrel/django-nonrel

5. Copiar a pasta `django` do repositório para a pasta lib do Python instalado,

  ```bash
  Copiar a pasta "django-nonrel/django" para "C:\Python27\Lib"
  ```
