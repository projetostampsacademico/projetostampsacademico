from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import JsonResponse
from nosql.service import MongoService
from pprint import pprint


# Create your views here.

def index(request, template_name='disease/index.html'):
    """Index page."""
    service = MongoService.Instance()
    collections = service.collection_names()
    # data = service.fetch_data()
    return render(request, template_name, {'collections': collections})


def database(request, template_name='disease/database.html'):
    """Database page."""
    service = MongoService.Instance()
    collections = service.collection_names()
    # data = service.fetch_data()
    return render(request, template_name, {'collections': collections})


def list(request, template_name='disease/list.html'):
    """Collection list page."""
    service = MongoService.Instance()
    collection = request.GET['collection']
    data = service.fetch_data(collection)
    return render(request, template_name, {'collection': collection, 'data': data})


def query(request, template_name='disease/list.html'):
    """Query disease list page."""
    disease_code = request.GET['code']
    return redirect("http://apps.who.int/classifications/icd10/browse/2016/en#/" + disease_code)
