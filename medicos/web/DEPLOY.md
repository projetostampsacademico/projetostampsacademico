Projeto STAMPS - TS#02 Segmento Médico
=======================================

Guia para Deploy no Heroku
---------------------------

1. Logar com heroku

```bash
heroku login
```

2. Submeter mudanças usando git. Na raiz do projetostampsacademico:

```bash
git subtree push --prefix medicos/web heroku master
```

3. Se tiver migrações no banco:

(Localmente antes do deploy)

```bash
python manage.py makemigrations [módulo]
```

(No Heroku depois do deploy)

```bash
heroku run bash
```

```bash
python manage.py migrate
```
