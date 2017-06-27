Projeto STAMPS - TS#02 Segmento Médico
=======================================

Guia do projeto Django
----------------------

Referências:
- [O que é Django?](https://tutorial.djangogirls.org/pt/django/)
- [Documentação Oficial](https://www.djangoproject.com/)


Tutorial
--------


1. Estrutura de projeto e arquivos

Na raiz do projeto Django, temos os arquivos:
- **requirements.txt** são as dependências (libraries externas) do projeto
- **manage.py** interface do projeto Django, usada para rodar o servidor, realizar migrações, etc
- **static** é a pasta de todos os arquivos estáticos (imagens, js, css)

Temos também duas pastas, ou módulos. A pasta com nome do projeto (web) é o núcleo da aplicação:
- **settings.py** são as configurações gerais (mexer com cautela)
- **urls.py** são as rotas da aplicação web
- **views.py** é o controller da aplicação, responsável por renderizar as views
- **templates** é uma pasta onde estão as views da aplicação

A outra pasta (módulo register) tem arquivos muito parecidos:
- **urls.py**, **views.py**, **templates**
- **migrations** são as migrações, útil quando o BD é relacional
- **models.py** são todos os models do projeto, especificados como objetos (ORM)


2. Codificando em python

Geralmente para desenvolver uma nova página web, é criada uma nova rota em **urls.py**:


```bash
default_urls  = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^uma-nova-rota-adicionada/', views.acao_descrita_no_arquivo_views)
]
```

Em seguida, adicionar a ação do arquivo **views.py**:

```bash
def index(request):
    """Index page."""
    # Algoritmo em python
    return render_to_response(
        'web/arquivo_html_a_ser_adicionado.html', context_instance=RequestContext(request))
```

Basta então adicionar o arquivo html na pasta templates. Em seguida executar o servidor e observar o resultado.
