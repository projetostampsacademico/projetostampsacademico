from django.shortcuts import render, render_to_response
from django.template import RequestContext
from nosql.service import MongoService

# Create your views here.

def index(request, template_name='nosql/index.html'):
    """Index page."""
    service = MongoService()
    collections = service.collection_names()
    data = service.fetch_data()
    return render(request, template_name, {'data': data, 'collections': collections})
