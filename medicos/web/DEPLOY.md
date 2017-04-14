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
